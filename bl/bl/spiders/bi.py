# -*- coding: utf-8 -*-
import re
import time
from copy import deepcopy
import scrapy
import json
from bl.items import BlItem


class BiSpider(scrapy.Spider):
    name = 'bi'
    allowed_domains = ['bilibili.com']
    # start_urls = ['http://bilibili.com/']

    def start_requests(self):
        room_id = '72956117'
        num = '9'
        urls = [f'https://api.bilibili.com/x/space/arc/search?mid={room_id}&ps=30&tid=0&pn={i}&keyword=&order=pubdate&jsonp=jsonp' for i in range(1,int(num)+1)]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        item  = BlItem()
        data = json.loads(response.text)
        for i in data['data']['list']['vlist']:
            item['bvid'] = i['bvid']
            item['title'] = i['title']
            item['length'] = i['length']
            item['created'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i['created']))
            item['play'] =  i['play']
            item['comment'] = i['comment']
            url = 'https://www.bilibili.com/video/' + i['bvid']
            yield scrapy.Request(url=url,callback=self.second_parse,meta={'Meta':deepcopy(item)})

    def second_parse(self,response):
        item = response.meta['Meta']
        try:
            vedio_url = re.search('window.__playinfo__=.*?"id":80,"baseUrl":"(.*?)",.*?}',response.text,re.S).group(1)
            audio_url = re.search('window.__playinfo__=.*?"id":30280,"baseUrl":"http(.*?)",.*?}',response.text,re.S).group(1)
            audio_url = 'https' + audio_url
            li = {
                'vedio':vedio_url,
                'audio':audio_url,
            }
            for name ,file_urls in li.items():
                item['name'] = name + '.m4s'
                item['file_urls'] =[file_urls]

                yield item
        except:
            pass



