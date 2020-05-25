# -*- coding: utf-8 -*-
import io

import pytesseract
import requests
import scrapy
import re

from PIL import Image

from ziru.items import ZiruItem


class ZiruSpider(scrapy.Spider):
    name = 'ziru'
    allowed_domains = ['ziroom.com']
    start_urls = ['http://www.ziroom.com/z/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',

    }

    def parse(self, response):
        check_picture = re.findall('url\((.*?)\);',response.xpath('/html/body/section/div[3]/div[2]/div[1]/div[2]/div[2]/span[2]/@style').get())
        check_picture_url = 'http:' + check_picture[0]
        num_list = list(self.get_picture(check_picture_url))
        print(check_picture_url)
        print(num_list)
        for i in response.xpath('//div[@class="item"]'):
            item = ZiruItem()
            try:
                item['title'] = i.xpath('./div[@class="info-box"]/h5/a/text()').get()
                item['desc'] = i.xpath('./div[@class="info-box"]/div[1]/div/text()').get()
                item['location'] = i.xpath('./div[@class="info-box"]/div[1]/div[2]/text()').get().strip()

                item['lable'] = ' | '.join(i.xpath('./div[@class="info-box"]/div[3]/span/text()').getall())
                el = i.xpath('./div[@class="info-box"]/div[2]/span/@style').getall()
                pirse_list = []
                for num in el:
                    num = int(float(re.findall('background-position: -(.*?)px',num)[0])/21.4)
                    pirse_list.append(num_list[num])
                item['pirse'] = ''.join(pirse_list) + str(i.xpath('./div[@class="info-box"]/div[2]/span[last()]/text()').get())
                yield item
            except AttributeError:
                pass
        next_url = response.xpath('//div[@class="Z_pages"]/a[last()]/@href').get()
        if next_url:
            next_url = 'http:' + next_url
            yield scrapy.Request(url=next_url,callback=self.parse)


    def get_picture(self,check_picture_url):
        r = requests.get(url=check_picture_url,headers=self.headers)
        if r.status_code ==200:
            image_stream = Image.open(io.BytesIO(r.content))
            testdata_dir_config = '--tessdata-dir "F:\\Tesser\\Tesseract-OCR\\tessdata"'
            print(pytesseract.image_to_string(image_stream, config=testdata_dir_config))
            return pytesseract.image_to_string(image_stream, config=testdata_dir_config)