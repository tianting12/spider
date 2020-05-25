# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import csv
import pymysql

# 定义管道写入csv文件数据
class ZhihuPipeline(object):

    def open_spider(self, spider):
        print('开始运行')

    def process_item(self,item,spider):
        pass
    def close_spdir(self,spdir):
        print('运行结束')


class ZhihuMysqlPipeline(object):
    def __init__(self):

        self.conn = pymysql.Connect(
            host='127.0.0.1',
            user='root',
            password='123456',
            database='czxy',
            port=3306,
            charset='utf8'
        )

        self.cursor = self.conn.cursor()


    def process_item(self,item,spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['\"%s\"'%i for i in data.values()])
        sql = 'insert into %s(%s) values (%s)'%('zhihu',keys,values)
        print(item)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

