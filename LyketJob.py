import feedparser
import time
import thread
import json
from MongoLib import *
from multiprocessing.dummy import Pool as ThreadPool 
import datetime
from NewsArticle import NewsArticle
class LyketJob:
	def __init__(self):
		self.file=open('LikeItRSSFeeds.txt')
		self.db=MongoLib("lyket", "articles")

	#thread function, will put enteries into DB in paraell. Will build json, then put into DB
	def put_article_in_db(self,story_url):
		current_article = NewsArticle(story_url)
		

		
		#publish date for article : datetime object 
		article_published = current_article.date_made()
		
		

		#title of article : String
		article_title=current_article.get_title()



		



		if(list(self.db.CollectionFind({'title': article_title, 'pub': article_published}))):
			print "entry already found in DB title: " + article_title 
		else:
			current_article.goodArticle()
			#keywords in article: Array of Strings
			article_key_words = current_article.getKeywords()
			
			#videos in story : Array of Strings (url to videos)
			article_videos = current_article.get_videos()


			#summary of article : String
			article_summary = current_article.getSummary()
			
			#authors of article: Array of Strings
			article_authors = current_article.getAuthors()
			
			#image for article : String (url to image)
			article_thumbnaillink = current_article.thumbnail_url()

			article_url = current_article.get_url()


			new_entry = {}
			new_entry['title']=article_title
			new_entry['sum']=article_summary
			new_entry['auth']=article_authors
			new_entry['thumb'] = article_thumbnaillink
			new_entry['pub'] = article_published
			new_entry['keywords'] = article_key_words
			new_entry['vids']  = article_videos
			new_entry['likes']=0
			new_entry['dislikes']=0
			new_entry['comments'] = []
			new_entry['url'] = article_url
			new_entry['creationtime']=datetime.datetime.now()
			self.db.CollectionSubmitOne(new_entry)
		





	def runJob(self):
		try:
			pool = ThreadPool(8)
			url_array=[]
			for stream in self.file:

				currentstream = feedparser.parse(stream)
				for entry in currentstream['entries']:
					story_url = entry['link']
					url_array.append(story_url)
					
				result = pool.map(self.put_article_in_db, url_array)
				url_array=[]
		except Exception as e:
			print "The following issue occured: "
			print e
			print " "

					
			


x=LyketJob()
x.runJob()
			