import re
from scrapy.http import Request
from scrapy.spiders import BaseSpider
from scrapy.selector import Selector
from first_crawler.items import FirstCrawlerItem

class FirstSpider(BaseSpider):
	name = 'First_Crawler'
	allowed_domains = ['packtpub.com']
	start_urls = ["https://www.packtpub.com"]
	"""docstring for ClassName"""
	def parse(self, response):
		xpath_extract=Selector(response)

		book_titles = xpath_extract.xpath('//div[@class="book-block-title"]/text()').extract()
		for title in book_titles:
			book = FirstCrawlerItem()
			book["title"] = title
			yield book

# array of visited links and avoiding repeated visiting of links 
		visited_links=[]
		links=xpath_extract.xpath('//a/@href').extract()
		url_validation= re.compile("^(?:http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")
		for link in links:
			if url_validation.match(link) and not link in visited_links:
				visited_links.append(links)
				yield Request(link,self.parse)
			else:
				full_url=response.urljoin(link)
				visited_links.append(full_url)
				yield Request(full_url,self.parse)