import feedparser
import time
import thread
import json
from MongoLib import *

from NewsArticle import NewsArticle
class LyketJob:
	def __init__(self):
		self.file=open('LikeItRSSFeeds.txt')
		self.db=MongoLib("Lyket", "Articles")

	#thread function, will put enteries into DB in paraell. Will build json, then put into DB
	def put_article_in_db(self,article_tuple):
		new_entry = {}
		new_entry['art_sum']=article_tuple[0]
		new_entry['art_auth']=article_tuple[1]
		new_entry['art_thumb'] = article_tuple[2]
		new_entry['art_pub'] = article_tuple[3]
		new_entry['art_key_words'] = article_tuple[4]
		new_entry['art_vids']  = article_tuple[5]
		new_entry['likes']=0
		new_entry['dislikes']=0
		new_entry['comments'] = []



		self.db.CollectionSubmitOne(new_entry)
		print str(article_tuple[2])





	def runJob(self):
		try:
			for stream in self.file:

				currentstream = feedparser.parse(stream)
				for entry in currentstream['entries']:
					story_url = entry['link']
					current_article = NewsArticle(story_url)
					

					#summary of article : String
					article_summary = current_article.getSummary()
					
					#authors of article: Array of Strings
					article_authors = current_article.getAuthors()
					
					#image for article : String (url to image)
					article_thumbnaillink = current_article.thumbnail_url()
					
					#publish date for article : datetime object 
					article_published = current_article.date_made()
					
					#keywords in article: Array of Strings
					article_key_words = current_article.getKeywords()
					
					#videos in story : Array of Strings (url to videos)
					article_videos = current_article.get_videos()
					
					#make json out of these parameters and put into db.
					thread.start_new_thread(self.put_article_in_db, ((article_summary,article_authors,article_thumbnaillink,article_published, article_key_words,article_videos), ))
		except Exception as e:
			print "The following issue occured: "
			print e
			print " "

					
			


x=LyketJob()
x.runJob()
			