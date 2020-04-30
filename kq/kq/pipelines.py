# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class KqPipeline(object):

    def process_item(self, item, spider):
        return item


class KqFileCsvPipeline(object):
    def __init__(self):
        self.file = open('kq.csv','a',encoding='utf-8',newline='')
        self.csvWriterr = csv.writer(self.file)
        self.csvWriterr.writerow(['工作名字','工作类别','经验要求','年龄要求','性别要求','招聘人数','学历要求','岗位性质','每周休息','薪酬范围','发布时间','承诺月薪','工作地点','薪资待遇','职位要求','负责人','电话','qq','微信','邮箱','公司','','位置','公交',])

    def process_item(self,item,spider):

        data = [
            item.get('jobName',''),
            item.get('leibie','').strip(),
            item.get('jingyan','').strip(),
            item.get('age','').strip(),
            item.get('gender','').strip(),
            item.get('num','').strip(),
            item.get('xueli','').strip(),
            item.get('jobxingzhi','').strip(),
            item.get('meihzouxiuxi','').strip(),
            item.get('salary','').strip(),
            item.get('fabushijian','').strip(),
            item.get('chengnuoyueyin','').strip(),
            item.get('gongzuodidian','').strip(),
            item.get('xinzidaiyu','').strip() if item.get('xinzidaiyu','') else  '',
            # ','.join(b.strip() for b in item.get('jobyaoqiu','')),
            item.get('jobyaoqiu','').strip(),
            item.get('fZeRen','').strip() if item.get('fZeRen','').strip() else '',
            item.get('phone','').strip() if item.get('phone','') else '',
            item.get('qq','').strip()  if item.get('qq','') else '',
            item.get('vx','').strip()  if item.get('vx','') else '',
            item.get('mailBox','').strip()  if item.get('mailBox','')  else '',
            item.get('companyName','').strip()  if item.get('companyName','') else '',
            item.get('Location','').strip()  if item.get('Location','') else '',
            item.get('transit','').strip()  if item.get('transit','') else '',

        ]
        print(data)
        self.csvWriterr.writerow(data)

    def close_spider(self,spider):
        self.file.close()

