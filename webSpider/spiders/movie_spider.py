import scrapy

class MSpider(scrapy.Spider):
    name = "mspider"
    allowed_domains = ["ygdy8.net"]
    start_urls = [
        "http://www.ygdy8.net/html/gndy/dyzz/index.html"
    ]
    base_url = "http://www.ygdy8.net/html/gndy/dyzz/"

    def parse(self, response):
	titles = response.xpath('//table[@class="tbspan"]/tr[2]/td[2]/b/a/text()').extract()
        pages = len( response.xpath('//*[@name="sldd"]//option/text()').extract())
        urls  = response.xpath('//*[@name="sldd"]//option/@value').extract()
        print "number of pages:", pages
#       for t in titles:
#	    print t.encode('utf-8')
#       for u in urls:
#          print "".join([MSpider.base_url,u])

        for i in range(1,3):
            url = "".join([MSpider.base_url,urls[i]])
            print "parsing:",url
            yield scrapy.Request(url,callback=self.parsePage)

    def parsePage(sel,response):
        titles = response.xpath('//table[@class="tbspan"]/tr[2]/td[2]/b/a/text()').extract()
        for t in titles:
            print t.encode('utf-8')
        return 
