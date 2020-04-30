# -*- coding: utf-8 -*-
import scrapy

from ahxgshang.items import AhxgshangItem


class GongshangSpider(scrapy.Spider):
    name = 'gongshang'
    allowed_domains = ['gongshang.mingluji.com']
    start_urls = ['https://gongshang.mingluji.com/anhui/riqi']

    def parse(self, response):

        urls = response.xpath('//*[@id="block-system-main"]/div/div/div[2]/table/tbody/tr/td/div/span/a/@href').getall()
        for url in urls:
            url = 'https://gongshang.mingluji.com' + url
            yield scrapy.Request(url=url,callback=self.second_parse)

        next_url = response.xpath('//*[@id="block-system-main"]/div/div/div[3]/ul/li[3]/a/@href').get()

        if next_url:
            next_url = 'https://gongshang.mingluji.com' + next_url
            yield scrapy.Request(url = next_url,callback=self.parse)

    def second_parse(self,response):
        companyUrls = response.xpath('//*[@id="block-system-main"]/div/div/div[2]/table/tbody/tr/td[1]/a/@href').getall()

        for companyUrl in companyUrls:
            yield scrapy.Request(url= companyUrl,callback=self.get_info)

        next_url = response.xpath('//*[@id="block-system-main"]/div/div/div[3]/ul/li[3]/a/@href').get()
        if next_url:
            next_url = 'https://gongshang.mingluji.com' + next_url
            yield scrapy.Request(url =next_url,callback=self.second_parse)

    def get_info(self,response):


        item = AhxgshangItem()
        info = response.xpath('//*[@id="block-system-main"]/div/div/div/div/div/fieldset[1]/div/ul')

        item['name'] = info.xpath('./li[1]/span[2]/span/text()').get()
        item['ID'] = info.xpath('./li[2]/span[2]/span/a/text()').get()
        item['registeredAddress'] = info.xpath('./li[3]/span[2]/span/text()').get()
        item['registeredTime'] = info.xpath('./li[4]/span[2]/span/a/text()').get()
        item['legalPerson'] = info.xpath('./li[5]/span[2]/span/a/text()').get()
        item['businessScope'] = info.xpath('./li[6]/span[2]/span/text()').get()
        item['area'] = info.xpath('./li[7]/span[2]/span/a/text()').get()
        item['city'] = info.xpath('./li[8]/span[2]/span/a/text()').get()
        item['category'] = info.xpath('./li[8]/span[2]/span/a/text()').get()
        item['companyType'] = info.xpath('./li[10]/span[2]/span/text()').get()
        item['companyStatus'] = info.xpath('./li[11]/span[2]/span/text()').get()

        yield item




