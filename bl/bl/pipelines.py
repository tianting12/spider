# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from copy import deepcopy

from scrapy.pipelines.files import FilesPipeline
import scrapy
from scrapy.exceptions import DropItem

class BlPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            yield scrapy.Request(url=file_url,meta={'Meta':deepcopy(item)})

    def file_path(self, request, response=None, info=None):
        data = request.meta['Meta']
        full = data.get('title')
        media_guid = data.get('name')
        full = full.replace(' ','')

        return f'{full}/{media_guid}'