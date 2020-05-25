# -*- coding: utf-8 -*-
import base64
from copy import deepcopy

import pytesseract
import scrapy
from gxrc.items import GxrcItem
import requests
import io
try:
    from PIL import Image
except:
    import Image

class GxrcSpider(scrapy.Spider):
    name = 'gxrc'
    allowed_domains = ['www.gxrc.com']
    # start_urls = ['https://s.gxrc.com/sJob?schType=1&expend=1&PosType=5955']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    }
    def start_requests(self):
        urls = [f'https://s.gxrc.com/sJob?schType=1&expend=1&PosType={i}' for i in range(5833,5958)]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)
    def parse(self, response):

        for li in response.xpath('//div[@class="rlOne"]'):
            item = GxrcItem()
            item['job_name'] = li.xpath('./ul[1]/li[1]/h3/a/text()').get()
            item['company'] = li.xpath('./ul[1]/li[2]/a/text()').get()
            item['salary'] = li.xpath('./ul[1]/li[3]/text()').get()
            item['location'] = li.xpath('./ul[1]/li[4]/text()').get()
            item['release_time'] = li.xpath('./ul[1]/li[5]/text()').get()
            item['num'] = '招聘' + str(li.xpath('./ul[2]/li[1]/span/text()').get()) + '人'
            # print(type(str(li.xpath('./ul[2]/li[2]/span/text()').get())))
            item['education'] = '学历:' + str(li.xpath('./ul[2]/li[2]/span/text()').get())
            item['experience'] = '经验:' + str(li.xpath('./ul[2]/li[3]/span/text()').get())
            item['company_type'] = li.xpath('./ul[2]/li[4]/span/text()').get()
            url = li.xpath('./ul[1]/li[1]/h3/a/@href').get()
            if url:
                url = 'https:' + url
                yield scrapy.Request(url=url,callback=self.second_parse,meta={'item':deepcopy(item)})

        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        if next_url:
            next_url = 'https://s.gxrc.com' + next_url
            yield scrapy.Request(url=next_url,callback=self.parse,dont_filter=True)

    def second_parse(self,response):

        item = response.meta['item']
        info = response.xpath('//*[@id="jobDetail"]/div[2]/div[1]/div[1]/div[5]/div[2]')
        item['contact'] = info.xpath('./p[1]/label/text()').get()
        contact_phone = info.xpath('./p[2]/label/img/@src').get()
        item['contact_mailbox'] = info.xpath('./p[3]/label/text()').get()
        item['contact_address'] = info.xpath('./p[4]/label/text()').get()

        try:
            item['contact_phone'] = self.Picture_recognition(contact_phone)
        except:
            item['contact_phone'] = 'None'
        # print(item)
        yield item



    def Picture_recognition(self,url):
        AppId = 18502209
        API_Key = 'yfaVb7kBnHX2HbXCxsWZsgYb'
        Secret_Key = 'uNhluTF0bXIKG3Cb3lG6EKFVfACpD6M4'
        url = 'https:' + url
        image_body = requests.get(url).content
        #tesseract 准确率低不高
        # image_stream = Image.open(io.BytesIO(image_body))
        # testdata_dir_config = '--tessdata-dir "F:\\Tesser\\Tesseract-OCR\\tessdata"'
        # return pytesseract.image_to_string(image_stream, config=testdata_dir_config)

        image_base64 = base64.b64encode(image_body)

        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_Key + '&client_secret=' + Secret_Key
        response = requests.get(host)
        request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

        access_token = response.json()['access_token']
        params = {"image": image_base64}
        # access_token = '24.63b84db5a05a0e35e7eb718b224bd35c.2592000.1584535773.282335-18502209'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json()['words_result'][0]['words'])
            return response.json()['words_result'][0]['words']
