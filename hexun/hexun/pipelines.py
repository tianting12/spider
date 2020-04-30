# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class HexunPipeline(object):

    def open_spider(self,spider):
        self.file = open('和讯理财.csv','a',encoding='utf-8',newline='')
        self.csvWriter =csv.writer(self.file)

    def process_item(self, item, spider):
        data = [
            item.get('title',''),
            item.get('timeResult', ''),
            item.get('url',''),
        ]
        self.csvWriter.writerow(data)
        return item

    def close_spider(self,spider):
        self.file.close()