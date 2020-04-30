# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FangtxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()
    house_size = scrapy.Field()
    house_area = scrapy.Field()
    house_louceng = scrapy.Field()
    house_chaoxiang = scrapy.Field()
    xiaoqu = scrapy.Field()
    weizhi = scrapy.Field()
    price = scrapy.Field()
