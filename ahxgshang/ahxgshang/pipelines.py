# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class AhxgshangPipeline(object):
    def process_item(self, item, spider):
        return item

class AhxgshangCsvFilePipeline(object):
    def __init__(self):
        self.file = open('anhui.csv','a',encoding='utf-8',newline='')
        self.csvWriter = csv.writer(self.file)
        self.csvWriter.writerow(['企业名称','统一社会信用代码/工商注册号','注册地址','注册日期','法定代表人','经营范围','地区','县市','分类','企业类型','公司现状',])

    def process_item(self, item, spider):
        data = [
            item.get('name',''),
            item.get('ID',''),
            item.get('registeredAddress',''),
            item.get('registeredTime',''),
            item.get('legalPerson',''),
            item.get('businessScope',''),
            item.get('area',''),
            item.get('city',''),
            item.get('category',''),
            item.get('companyType',''),
            item.get('companyStatus',''),
        ]
        self.csvWriter.writerow(data)
    def close_item(self,):
        self.file.close()