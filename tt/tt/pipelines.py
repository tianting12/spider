# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from copy import deepcopy

class TtPipeline(object):
    def process_item(self, item, spider):
        if item["final_price"]:
            item["final_price"] = item["final_price"].split(" ",1)
        return item

class TtImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_url']:
            yield scrapy.Request(image_url,meta={"name":deepcopy(item['name'])})

    def item_completed(self, results, item, info):
        # print([x['path'] for ok, x in results if ok] )
        image_paths = [x['path'] for ok, x in results if ok]  # ok判断是否下载成功
        if not image_paths:
            raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        return item
    def file_path(self,request,response=None,info=None):

        image_guid = request.url.split('/')[-1]
        # 接收上面meta传递过来的图片名称
        name = request.meta['name']
        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        #name=re.sub(r'[？\\*|"<>:/]', '', name)
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'{0}-{1}'.format(name,image_guid)
        return filename