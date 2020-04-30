# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TtItem(scrapy.Item):
    # define the fields for your item here like:
    b_cate = scrapy.Field()
    s_cate = scrapy.Field()
    s_href = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()
    was_price = scrapy.Field()
    final_price = scrapy.Field()
    cart_img = scrapy.Field()
    size = scrapy.Field()
    cart_galley_small_img = scrapy.Field()
    cart_content_img = scrapy.Field()
    # image_urls = scrapy.Field()
    image_url = scrapy.Field()
    images = scrapy.Field()


