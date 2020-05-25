# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymysql import Connect

class GxrcPipeline:
    def process_item(self, item, spider):
        return item

class GxrcMysqlPipeline:
    def __init__(self, host, database, port, user, password):
        self.host = host
        self.database = database
        self.table_name = 'gxrc'
        self.port = port
        self.user = user
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            port=crawler.settings.get('MYSQL_PORT'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),

        )

    def open_spider(self, spider):
        # print(self.table_name)
        self.db = Connect(
            host=self.host,
            database=self.database,
            port=self.port,
            user=self.user,
            password=self.password,
            charset='utf8',
        )
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['\"%s\"' % i for i in data.values()])
        sql = 'insert into %s(%s) values (%s)' % (self.table_name, keys, values)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print('异常错误是：', e)

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
