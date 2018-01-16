#scrapy runspider spider1.py

import scrapy
import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)

class spider1(scrapy.Spider):
    name = 'Wikipedia'
    start_urls = ['https://en.wikipedia.org/wiki/Battery_(electricity)']

   	def parse(self, response):
        pass

	def parse(self, response):
	        print response.css('h1#firstHeading::text').extract()
	        
	def parse(self, response):
	        print ''.join(response.css('div#mw-content-text>div>p')[0].css('::text').extract())
	def parse(self, response):
	        for e in response.css('div#mw-content-text>div>p'):
	            yield { 'para' : ''.join(e.css('::text').extract()).strip() }

	def parse(self, response):
	        for e in response.css('div#boxoffice>table>tbody>tr'):
	            yield {
	                'title': ''.join(e.css('td.titleColumn>a::text').extract()).strip(),
	                'weekend': ''.join(e.css('td.ratingColumn')[0].css('::text').extract()).strip(),
	                'gross': ''.join(e.css('td.ratingColumn')[1].css('span.secondaryInfo::text').extract()).strip(),
	                'weeks': ''.join(e.css('td.weeksColumn::text').extract()).strip(),
	                'image': e.css('td.posterColumn img::attr(src)').extract_first(),
	            }

