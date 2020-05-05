# -*- coding: utf-8 -*-
import re

import scrapy

from douban250.items import Douban250Item


class Douban250Spider(scrapy.Spider):
    name = 'douban250'
    allowed_domains = ['book.douban.com']
    start_urls = [f'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={20*i}&type=T' for i in range(25)]

    def parse(self, response):

        item = Douban250Item()

        for li in response.xpath('//li[@class="subject-item"]'):

            item['book_name'] = li.xpath('./div[2]/h2/a/text()').extract_first().strip()
            item['auther'] = li.xpath('./div[2]/div[1]/text()').extract_first().strip().split('/')[0]
            item['score'] = li.xpath('./div[2]/div[2]/span[2]/text()').get()
            comments_num = li.xpath('./div[2]/div[2]/span[3]/text()').get()
            item['comments_num'] = re.search('(\d+)',str(comments_num)).group(1)
            item['introduction'] = li.xpath('./div[2]/p/text()').get()
            item['image_url'] = li.xpath('./div[1]/a/img/@src').getall()
            yield item

        #爬全部就把下面的打开
        # next_url = response.xpath('//span[@class="next"]/a/@href').get()
        # if next_url:
        #     next_url = 'https://book.douban.com' + next_url
        #     yield scrapy.Request(url=next_url,callback=self.parse)

