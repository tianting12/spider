# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class WeiboPipeline:
    def process_item(self, item, spider):
        return item

class WeiboMongoPipeline(object):

    def __init__(self, mongodb_url, mongodb_db, mongodb_table_name):
        self.mongodb_url = mongodb_url
        self.mongodb_db = mongodb_db
        self.table_name = mongodb_table_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_url=crawler.settings.get('MONGODB_URL'),
            mongodb_db=crawler.settings.get('MONGODB_DB'),
            mongodb_table_name=crawler.settings.get('MONGODB_TABLE_NAME')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongodb_url)
        self.db = self.client[self.mongodb_db]

    def process_item(self, item, spider):
        self.db[self.table_name].insert(dict(item))
        print('插入成功')
        return item

    def close_spider(self, spider):
        self.client.close()