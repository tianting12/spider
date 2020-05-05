# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban250Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field() #书名
    auther = scrapy.Field() # 作者
    score = scrapy.Field()  #评分
    comments_num = scrapy.Field()   #评价人数
    introduction = scrapy.Field()# 小说简介
    image_url= scrapy.Field()# 封面图url
    images = scrapy.Field()
