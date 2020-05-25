# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class ZiruItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field() #标题
    desc = Field() # #描述
    location = Field() # 位置
    pirse = Field() #价格
    lable = Field() #标签
