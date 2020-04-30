# -*- coding: utf-8 -*-
import json
import re
from copy import deepcopy

import scrapy

from kq.items import KqItem


class Kq36Spider(scrapy.Spider):
    name = 'kq36'
    allowed_domains = ['kq36.com']
    # start_urls = ['https://www.kq36.com/job_list.asp?Job_ClassI_Id=2&provinceid=2&cityid=9']
    def start_requests(self):
        with open(r'G:/spdir/kq/kq/area/31.json', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                area = json.loads(line)
                url = f'https://www.kq36.com/job_list.asp?Job_ClassI_Id=2&provinceid={area["provinceid"]}&cityid={area["cityid"]}&areaid={area["areaid"]}'
                yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        item = KqItem()
        for info in response.xpath('//div[@class="contenter"]/div[1]/div/div[2]/div'):
            jobUrl = info.xpath('./div[@class="li_title"]/a/@href').get()
            item['jobName'] = info.xpath('./div[@class="li_title"]/a/text()').get()
            item['companyName'] = info.xpath('./div[@class="li_company"]/a/text()').get().strip()

            joburl = 'https://www.kq36.com' + jobUrl
            yield scrapy.Request(url=joburl, callback=self.job_info, meta=deepcopy({'item': item}))

        next_url = response.selector.re('</div><div .*? <a href=(.*?) title="下一页">')

        if next_url:
            next_url = 'https://www.kq36.com' + next_url[0][1:-1]
            yield scrapy.Request(url=next_url,callback=self.parse)

    def job_info(self,response):
        item = response.meta['item']
        trs = response.xpath('//div[@class="contenter"]/div[1]/div[1]/table[2]/tr/td/table/tr[3]/td/div/table/tr/td/table/tr/td/table')
        try:
            for tr in trs:
                item['fZeRen'] = tr.xpath('./tr[1]/td[1]/span[2]/text()').get()
                item['qq'] = tr.xpath('./tr[1]/td[2]/span[2]/text()').get()
                item['phone'] = tr.xpath('./tr[2]/td[1]/span[2]/text()').get()
                item['mailBox'] = tr.xpath('./tr[2]/td[2]/span[2]/text()').get()
                item['vx'] = tr.xpath('./tr[3]/td[1]/span[2]/text()').get()

                item['Location'] = tr.xpath('./tr[6]/td/div/table/tr/td/span[2]/text()').get()
                item['transit'] = tr.xpath('./tr[7]/td/table/tr/td[2]/span/text()').get()

        except Exception as e:
            print(e, '不是我们要爬取的内容')

        jobinfoes = response.xpath('//*[@id="wrap"]/div[7]/div[1]/div/table[1]/tr/td/table/tr[2]/td/table/tr[2]/td/table/tr/td/div/table/tr[2]/td/table')


        for jobinfo in jobinfoes:
            item['leibie'] = jobinfo.xpath('./tr[1]/td/table/tr/td[2]/div/a/span/text()').get()
            item['jingyan'] = jobinfo.xpath('./tr[1]/td[2]/span[2]/text()').get()
            item['age'] = jobinfo.xpath('./tr[2]/td[1]/span[2]/text()').get()
            item['gender'] = jobinfo.xpath('./tr[2]/td[2]/span[2]/text()').get()
            item['num'] = jobinfo.xpath('./tr[3]/td[1]/span[2]/text()').get()
            item['xueli'] = jobinfo.xpath('./tr[3]/td[2]/span[2]/text()').get()
            item['jobxingzhi'] = jobinfo.xpath('./tr[4]/td[1]/span[2]/text()').get()
            item['meihzouxiuxi'] = jobinfo.xpath('./tr[4]/td[2]/span[2]/text()').get()
            item['salary'] = jobinfo.xpath('./tr[5]/td[1]/span[2]/text()')[0].get()
            item['fabushijian'] = jobinfo.xpath('./tr[5]/td[2]/span[2]/text()').get()
            item['chengnuoyueyin'] = jobinfo.xpath('./tr[6]/td[1]/span[2]/text()').get()
            item['gongzuodidian'] = jobinfo.xpath('./tr[7]/td/span[2]/text()').get()

            item['xinzidaiyu'] = jobinfo.xpath('./tr[8]/td/span[2]/span/text()').get() if jobinfo.xpath('./tr[8]/td/span[2]/span/text()') else None
            item['jobyaoqiu'] = jobinfo.xpath('./tr[9]/td/table/tr/td[2]/div/text()').get() if jobinfo.xpath('./tr[9]/td/table/tr/td[2]/div/text()') else jobinfo.xpath('./tr[8]/td/table/tr/td[2]/div/text()').get()

            yield item





