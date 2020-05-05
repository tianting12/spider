# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import scrapy

class Douban250Pipeline(object):
    def process_item(self, item, spider):
        return item

class Douban250MongodbPipeline:
    def __init__(self,mongodb_url,mongodb_db,mongodb_table_name):
        self.mongodb_url =mongodb_url
        self.mongodb_db =mongodb_db
        self.mongodb_table_name =mongodb_table_name

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongodb_url=crawler.settings.get('MONGODB_URL'),
            mongodb_db=crawler.settings.get('MONGODB_DB'),
            mongodb_table_name=crawler.settings.get('MONGODB_TABLE_NAME')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongodb_url)
        self.db = self.client[self.mongodb_db]

    def process_item(self,item,spider):
        self.db[self.mongodb_table_name].insert_one(dict(item))
        return item

    def close_item(self,spider):
        self.client.close()

class Douban250ImagePipeline(ImagesPipeline):

    def get_media_requests(self,item,info):
        for image_url in item['image_url']:
            yield scrapy.Request(image_url, meta={"name":item['book_name']})

    def item_completed(self,results,item,info):
        image_paths = [x['path'] for ok, x in results if ok] # ok判断是否下载成功
        if not image_paths:
            raise DropItem('Item contains no images')
        item['file_paths'] = image_paths
        return item

    def file_path(self,request,response=None,info=None):

        filename = request.meta['name'] +'.jpg'
        return filename