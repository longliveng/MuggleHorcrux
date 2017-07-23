# -*- coding: utf-8 -*-
# from scrapy.mail import MailSender
import scrapy
# import sys
import time
import datetime
# import MySQLdb
import json


class DoubanStatusesSpider(scrapy.Spider):
    name = "DoubanStatuses"

    def start_requests(self):
        self.username = getattr(self, 'username', None)
        # https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy-spider
        # print({'form_email': self.settings['douban_account'], 'form_password':self.settings['douban_pwd']})
        # exit()
        return [scrapy.FormRequest("https://accounts.douban.com/login", formdata={'form_email': self.settings['DOUBAN_ACCOUNT'], 'form_password':self.settings['DOUBAN_PWD']}, callback=self.logged_in)]

    def logged_in(self, response):
        print('---------------this----------------------------')
        print(response)
        exit()
        resultUrl = []

        if self.username is None:
            # self.generateShanghai()
            # self.generateShenzhen()
            exit()
        else:
            return resultUrl
