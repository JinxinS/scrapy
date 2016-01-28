# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

class CoverSpider(scrapy.Spider):
    name = "cover"
    allowed_domains = ["store.oneplus.cn"]
    start_urls = (
        'http://store.oneplus.cn/items/0215000201/'
        ,'http://store.oneplus.cn/items/0211000401/'
        #,'http://store.oneplus.cn/items/0215001001/'
        )

    def parse(self, response):
        title = response.xpath('//*[@id="accDetail"]/div/div[2]/h1/text()').extract()
        av = response.xpath('//*[@id="accDetail"]/div/div[2]/div[2]/div/a/text()').extract()
        content = av[0].encode('utf8')
        print bcolors.WARNING,title[0].encode('utf8'),":",bcolors.ENDC
        if content.decode('utf8') == u'到货通知':       
            print bcolors.FAIL, "item not available ", str(datetime.now()),bcolors.ENDC
        else:
            print bcolors.OKBLUE,"item is available!!! ", str(datetime.now()),bcolors.ENDC

