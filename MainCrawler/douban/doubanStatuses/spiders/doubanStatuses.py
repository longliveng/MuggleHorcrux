# -*- coding: utf-8 -*-
# from scrapy.mail import MailSender
import datetime
import json
# import sys
import time

import pymysql.cursors
import scrapy
from scrapy.selector import Selector


class DoubanStatusesSpider(scrapy.Spider):
    name = "DoubanStatuses"

    def __init__(self, *args, **kwargs):
        super(DoubanStatusesSpider, self).__init__(*args, **kwargs)
        self.aboutMysql()        

    def aboutMysql(self):
        # Connect to the database
        self.dbCon = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='cyhcyh',
            db='muggle_horcrux',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

        self.DBcursor = self.dbCon.cursor()

    # python3 -m scrapy crawl DoubanStatuses -a username=cyh1985
    def start_requests(self):
        username = getattr(self, 'username', None)
        self.username=username

        # for pageNo in range(1, 1501):
        for pageNo in range(1, 2):
            urlNow = 'https://www.douban.com/people/%s/statuses?p=%s' % (username,pageNo)
            urlNow.format(username, pageNo)

            yield scrapy.Request(url=urlNow, callback=self.stupidParse, cookies={'bid': self.settings['BID'], 'dbcl2': self.settings['DBCL2']})

    def stupidParse(self, response):

        print('---------------this----------------------------1111')
        
        # result = self.DBcursor.fetchone()
        print(response)
        for itemStatus in response.xpath('//div[contains(@class,"new-status")]').extract():
            itemUrl=Selector(text=itemStatus).css('.created_at a::attr(href)').extract_first()
            itemDate=Selector(text=itemStatus).css('.created_at::attr(title)').extract_first()

            itemImgUrl=Selector(text=itemStatus).css('.group-pic a::attr(href)').extract()

            itemImgUrl=",".join(itemImgUrl)

            # print(itemUrl)
            # print(type(itemUrl))

            # print(self.username)
            # print(type(self.username))

            # print(itemImgUrl)
            # print(type(itemImgUrl))

            
            # exit()
            sqlAdd = "INSERT INTO `sns_item`(`content`,`url`,`item_date`,`platform`,`account`,`img_url`,`img_path`)VALUES(%s,%s,%s,%s,%s,%s,%s);"
            
            # todo itemStatus 转义
            self.DBcursor.execute(sqlAdd, (itemStatus, itemUrl,itemDate, '1',self.username,itemImgUrl,''))
            self.dbCon.commit()


    def closed(self, reason):
        self.dbCon.close()
