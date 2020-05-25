# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class ZiruPipeline:
    def process_item(self, item, spider):
        return item

class ZiruMongoPipeline(object):
    def __init__(self,mongodb_url,mondodb_db,mondodb_table):
        self.mongodb_url = mongodb_url
        self.mondodb_db = mondodb_db
        self.mondodb_table = mondodb_table

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongodb_url=crawler.settings.get('MONGODB_URL'),
            mondodb_db=crawler.settings.get('MONGODB_DB'),
            mondodb_table=crawler.settings.get('MONGODB_TABLE'),
        )

    def open_spider(self,spider):
        self.client = MongoClient(self.mongodb_url)
        self.db = self.client[self.mondodb_db]

    def process_item(self,item,spider):
        self.db[self.mondodb_table].insert_one(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()

