# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() #文章标题
    bvid = scrapy.Field() # 视频bv号
    length = scrapy.Field() # 视频长度
    comment = scrapy.Field() # 文章评论数
    play = scrapy.Field() #播放量
    created = scrapy.Field() #发布时间
    vedio_url = scrapy.Field() #视频地址
    audio_url = scrapy.Field() #音频地址
    name = scrapy.Field()
    files = scrapy.Field()
    file_urls = scrapy.Field()