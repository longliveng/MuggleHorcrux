# -*- coding: utf-8 -*-
# from scrapy.mail import MailSender
import scrapy
# import sys
import time
import datetime
import json
import pymysql.cursors


class DoubanStatusesSpider(scrapy.Spider):
    name = "DoubanStatuses"

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
        self.aboutMysql()

        username = getattr(self, 'username', None)

        # for pageNo in range(1, 1501):
        for pageNo in range(1, 2):
            urlNow = 'https://www.douban.com/people/%s/statuses?p=%s' % (username,pageNo)
            urlNow.format(username, pageNo)

            yield scrapy.Request(url=urlNow, callback=self.stupidParse, cookies={'bid': self.settings['BID'], 'dbcl2': self.settings['DBCL2']})

    def stupidParse(self, response):

        print('---------------this----------------------------')
        print(response)
        exit()
        
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        self.DBcursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        connection.commit()

    def closed(self, reason):
        self.dbCon.close()
