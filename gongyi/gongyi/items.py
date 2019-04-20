# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GongyiItem(scrapy.Item):
    # define the fields for your item here like:
    status = scrapy.Field() 
    source = scrapy.Field() 
    title = scrapy.Field()  # 标题
    eOrgName = scrapy.Field()  # 发起方
    pName = scrapy.Field()  # 执行方
    proj_budget = scrapy.Field()  # 预算
    fundName = scrapy.Field()  # 公募
    url = scrapy.Field()  # url
    pass
