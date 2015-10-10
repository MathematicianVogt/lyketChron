import newspaper
from newspaper import Article
class Article:
	def __init__(self,url):
		self.article=Article(url)
		self.article.download()
		self.article.parse()
		self.article.nlp()
	
	def getKeywords(self):
		x=self.article.keywords
		for i in range(0,len(x)):
			x[i]=x[i].encode('ascii', 'ignore')
		return x

		return self.article.keywords
	def getSummary(self):
		return self.article.summary.encode('ascii', 'ignore')
	def getAuthors(self):
		x=self.article.authors
		for i in range(0,len(x)):
			x[i]=x[i].encode('ascii', 'ignore')
		return x
	def thumbnail_url(self):
		return self.article.top_image
	def date_made(self):
		return self.article.publish_date
