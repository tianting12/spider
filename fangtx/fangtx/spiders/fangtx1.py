#_*_coding:utf-8_*_
#作者       ：  Deth
#创建时间    : 2020/3/29 18:01
#文件       ： ftx. py
# IDE       : PyCharm
import scrapy
import re

from fangtx.items import FangtxItem


class FangTX(scrapy.Spider):
    name = 'fangtx'

    allowed_domains = ['xian.esf.fang.com']

    start_urls = ['https://xian.esf.fang.com/']

    def parse(self, response):

        for info in response.xpath('//dl[@class="clearfix"]'):

            item = FangtxItem()
            item['title'] = info.xpath('./dd/h4/a/span/text()').get()
            infoes = info.xpath('.//p[@class="tel_shop"]/text()').getall()
            infoes = list(map(lambda x: re.sub(r"\s", "", x), infoes))
            for house in infoes:

                if '室' in house:
                    item["house_size"] = house
                elif '层' in house:
                    item["house_louceng"] = house
                elif '向' in house:
                    item["house_chaoxiang"] = house
                elif '㎡' in house:
                    item['house_area'] = house

            # item['house_size'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[0].strip()
            # item['house_area'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[1].strip()
            # item['house_louceng'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[2].strip()
            # item['house_chaoxiang'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[3].strip()
            item['xiaoqu'] = info.xpath('//p[@class="add_shop"]/a/text()').extract()[0].strip()
            item['weizhi'] = info.xpath('//p[@class="add_shop"]/span/text()').extract()[0]
            price_s = info.xpath('.//dd[@class="price_right"]/span/b/text()').get()
            price_w = info.xpath('.//dd[@class="price_right"]/span[1]/text()').get()
            if price_s and price_w:
                item['price'] = ''.join(price_s) + ''.join(price_w)
            else:
                item['price'] = '暂无数据'

            yield item

        next_url = response.xpath('//*[@id="list_D10_15"]/span/following-sibling::p[1]/a/@href').get()
        print(next_url)
        if next_url:
            next_url = 'https://xian.esf.fang.com' + next_url
            yield scrapy.Request(url=next_url,meta={
                'dont_redirect': True,
                'handle_httpstatus_list': [302]
            },callback=self.parse, dont_filter=True)

