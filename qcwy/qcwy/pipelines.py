# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
from pymysql import Connect
from pymongo import MongoClient

class QcwyPipeline:
    def process_item(self, item, spider):
        return item

#MYSQL 存储
class QcwyMysqlPipeline(object):
    def __init__(self,host,database,port,user,password):
        self.host = host
        self.database = database
        self.table_name = '51job'
        self.port = port
        self.user = user
        self.password = password


    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            port=crawler.settings.get('MYSQL_PORT'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),

        )
    def open_spider(self,spider):
        # print(self.table_name)
        self.db = Connect(
            host = self.host,
            database = self.database,
            port = self.port,
            user = self.user,
            password = self.password,
            charset = 'utf8',
        )
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['\"%s\"' % i for i in data.values()])
        sql ='insert into %s(%s) values (%s)'%(self.table_name,keys,values)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print('异常错误是：',e)
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()

#mongodb存储
class QcwyMongodbPipeline(object):
    def __init__(self,mongodb_url,mongodb_db,mongodb_table):
        self.mongodb_url = mongodb_url
        self.mongodb_db = mongodb_db
        self.mongodb_table = mongodb_table

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongodb_url=crawler.settings.get('MONGODB_URL'),
            mongodb_db=crawler.settings.get('MONGODB_DB'),
            mongodb_table=crawler.settings.get('MONGODB_TABLE'),
        )
    def open_spider(self,spider):
        self.client = MongoClient(self.mongodb_url)
        self.db = self.client[self.mongodb_db]

    def process_item(self,item,spider):
        self.db[self.mongodb_table].insert_one(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()

#csv存储
class QcwyCsvPipeline(object):
    def __init__(self):
        self.file = open('qcxy.csv','a',encoding='utf-8',newline='')
        self.csvwriter = csv.writer(self.file)
        self.csvwriter.writerow(['职位','薪资','学历','工作经验','需要几人','工作地址','公司','公司类型',
                                 '公司规模','公司行业','福利','职位描述','职位要求','职位链接',])

    def process_item(self,item,spider):
        data = [
            item.get('jobName',''),
            item.get('salary',''),
            item.get('education',''),
            item.get('workExperience',''),
            item.get('needNumPeople',''),
            item.get('workAddress', ''),
            item.get('company',''),
            item.get('companyType',''),
            item.get('companySize',''),
            item.get('companyIndustry',''),
            item.get('fuli', ''),
            item.get('description',''),
            item.get('jobRequire',''),
            item.get('jobUrl','')
        ]
        self.csvwriter.writerow(data)

    def close_spider(self,spider):
        self.file.close()












