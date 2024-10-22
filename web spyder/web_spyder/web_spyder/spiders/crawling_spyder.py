from scrapy.spiders import CrawlSpider , Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
 name = "spider"
 allowed_domains = ["ketabrah.ir"]
 start_urls = ["https://ketabrah.ir"]
 rules = (
   Rule (LinkExtractor(allow="free-books-audiobooks"), callback="extract_data"),
 
 )
 
 def extract_data(self, response):
   yield{
     "title": response.css(".cell h3 a::text").getall()
   }