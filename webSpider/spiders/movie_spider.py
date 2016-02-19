# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import scrapy
from webSpider.items import WebspiderItem
class MSpider(scrapy.Spider):
    name = "mspider"
    allowed_domains = ["ygdy8.net"]
    start_urls = [
        "http://www.ygdy8.net/html/gndy/dyzz/index.html"
    ]
    base_url = "http://www.ygdy8.net/html/gndy/dyzz/"

    def parse(self, response):
#	titles = response.xpath('//table[@class="tbspan"]/tr[2]/td[2]/b/a/text()').extract()
        pages = len( response.xpath('//*[@name="sldd"]//option/text()').extract())
        urls  = response.xpath('//*[@name="sldd"]//option/@value').extract()
#        for t in titles:
#	    print t.encode('utf-8')

        for i in range(0,2):
            url = "".join([MSpider.base_url,urls[i]])
#            print "parsing page:",i,":",url,"priority=",pages-i
            yield scrapy.Request(url,callback=self.parsePage,priority=pages-i)

    def parsePage(self,response):
        titles = response.xpath('//table[@class="tbspan"]/tr[2]/td[2]/b/a/text()').extract()
	urls   = response.xpath('//table[@class="tbspan"]/tr[2]/td[2]/b/a/@href').extract()
	for t,u in zip(titles,urls):
            yield scrapy.Request("".join(["http://www.ygdy8.net",u]),callback=self.parseMovie)		
	return 

    def parseMovie(self,response):
	item = WebspiderItem()
	item['name']  = response.xpath('//p[br]/text()').extract()[0].encode('utf-8')
	item['link'] =  response.xpath("//table/tbody/tr/td/a/@href").extract()[0].encode('utf-8')
        return item	
