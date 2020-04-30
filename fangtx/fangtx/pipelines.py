# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class FangtxPipeline(object):
    def process_item(self, item, spider):
        return item

class FangCsvPinpeline(object):
    def __init__(self):
        self.file = open('{city}.csv','a',encoding='utf-8',newline='')
        self.csvWriter = csv.writer(self.file)
        self.csvWriter.writerow(['title','house_size','house_area','house_louceng','house_chaoxiang','xiaoqu','weizhi','price','pricemi'])

    def process_item(self,item,spider):
        date = [
            item.get('title',''),
            item.get('house_size',''),
            item.get('house_area',''),
            item.get('house_louceng',''),
            item.get('house_chaoxiang',''),
            item.get('xiaoqu',''),
            item.get('weizhi',''),
            item.get('price',''),
            item.get('pricemi',''),
        ]
        self.csvWriter.writerow(date)

    def close_spider(self,spider):
        self.file.close()