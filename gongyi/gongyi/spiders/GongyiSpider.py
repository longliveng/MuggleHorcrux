# -*- coding: utf-8 -*-
from gongyi.items import GongyiItem
import scrapy
import time
import datetime
import pymysql.cursors
import json
import re
from scrapy.selector import Selector


class GongyiSpider(scrapy.Spider):
    name = "gongyi"
    statusDict = {1: '募捐中', 2: '执行中', 3: '已结束'}

    def __init__(self, *args, **kwargs):
        super(GongyiSpider, self).__init__(*args, **kwargs)
        # if self.updateDayNum <= 1:
        #     exit()

    def start_requests(self):
        # def qq(self):
        for s_status in range(1, 4):
            for pageNo in range(1, 101):
                urlQQ = 'https://ssl.gongyi.qq.com/cgi-bin/WXSearchCGI?ptype=stat&s_status=%s&jsoncallback=_CallbackSearch&s_status=1&s_tid=0&s_puin=&s_fid=&s_key=&p=%s&_=1555224178748' % (
                    s_status, pageNo)
                urlQQ.format(s_status, pageNo)

                qqRequest = scrapy.Request(
                    url=urlQQ,
                    callback=self.parseQQ
                )
                qqRequest.meta['status'] = self.statusDict[s_status]

                yield qqRequest

        # def alipay(self):
        print('-----------------  alialipay ------------------------')
        for pageNo in range(1, 51):
            urlAli = 'https://love.alipay.com/donate/itemList.htm?page=%s&&donateType=&itemClassified=&orderType=gmt_create_desc&donateShowName=' % (
                pageNo)
            urlAli.format(pageNo)

            yield scrapy.Request(
                url=urlAli,
                callback=self.aliDetailRequest
            )

    def aliDetailRequest(self, response):
        print('-----------------  aliDetailRequest ------------------------')
        for oneAli in response.css('.donate-item-default-more::attr(href)').getall():
            aliRequest = scrapy.Request(
                url=oneAli,
                callback=self.parseAli
            )
            aliRequest.meta['status'] = self.statusDict[1]
            aliRequest.meta['url'] = oneAli
            # exit()

            yield aliRequest

    def parseAli(self, response):
        print('-----------------  parse  ali ------------------------')
        eOrgName = response.css('.donate-list-info-puborg-text::text').get()
        eOrgName = re.compile(r'发布机构：', re.S).sub('', eOrgName)

        item = GongyiItem()
        item['status'] = response.meta['status']
        item['source'] = '蚂蚁金服'
        item['title'] = response.css('.donate-detail-title::text').get()
        item['eOrgName'] = eOrgName
        item['pName'] = ''
        item['proj_budget'] = '请看链接'
        item['fundName'] = '请看链接'
        item['url'] = response.meta['url']

        yield item

    def parseQQ(self, response):
        print('-----------------  parseQQ ------------------------')
        responseText = response.text[16:]
        responseText = responseText[:-1]
        resList = json.loads(str(responseText))

        for aProj in resList['plist']:
            item = GongyiItem()

            pureBudget = re.compile(r'<img', re.S).sub(
                '图片：', aProj['proj_budget'])
            pureBudget = re.compile(r'<[^>]+>', re.S).sub('', pureBudget)

            item['status'] = response.meta['status']
            item['source'] = '腾讯'
            item['title'] = aProj['title']
            item['eOrgName'] = aProj['eOrgName']
            item['pName'] = aProj['pName']
            item['proj_budget'] = pureBudget
            item['fundName'] = aProj['fundName']
            item['url'] = 'https://gongyi.qq.com/succor/detail.htm?id=' + aProj['id']

            yield item
