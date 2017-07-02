# -*- coding: utf-8 -*-
import division
# from scrapy.mail import MailSender
import scrapy
# import sys
import time
import datetime
import MySQLdb
import json


class DoubanStatusesSpider(scrapy.Spider):
    name = "DoubanStatuses"

    def start_requests(self):
        self.username = getattr(self, 'username', None)
        # https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy-spider
        return [scrapy.FormRequest("https://accounts.douban.com/login", formdata={'form_email': '', 'form_password': ''}, callback=self.logged_in)]

    def logged_in(self, response):
        resultUrl = []
        # here you would extract links to follow and return Requests for
        # each of them, with another callback

        if self.username is None:
            # self.generateShanghai()
            # self.generateShenzhen()
            exit()
        else:
            return resultUrl
