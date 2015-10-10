import feedparser
import time

from NewsArticle import NewsArticle
class LyketJob:
	def __init__(self):
		self.file=open('LikeItRSSFeeds.txt')


	def runJob(self):
		for stream in self.file:

			currentstream = feedparser.parse(stream)
			for entry in currentstream['entries']:
				story_url = entry['link']
				current_article = NewsArticle(story_url)
				article_summary = current_article.getSummary()
				article_authors = current_article.getAuthors()
				article_thumbnaillink = current_article.thumbnail_url()
				article_published = current_article.date_made()
				print article_thumbnaillink
				time.sleep(1)
			


x=LyketJob()
x.runJob()
			