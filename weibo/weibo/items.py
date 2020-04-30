# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() #昵称
    jianjie = scrapy.Field() #简介
    gender = scrapy.Field() #性别
    weibodengji = scrapy.Field() #微博等级
    weiboshu = scrapy.Field() #微博数
    fensishu = scrapy.Field() #粉丝数
    guanzhuzhe = scrapy.Field() #关注者
    chushengriqi = scrapy.Field() # 年龄
    location = scrapy.Field()   #地区
    xueli = scrapy.Field() #学历
    # hangye = scrapy.Field() # 行业