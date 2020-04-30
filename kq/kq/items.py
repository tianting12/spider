# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KqItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()  #工作名字
    leibie = scrapy.Field() #工作类别
    jingyan = scrapy.Field() # 	经验要求
    age = scrapy.Field() # 年龄要求
    gender = scrapy.Field() #性别要求
    num = scrapy.Field() #招聘人数
    xueli = scrapy.Field() #	学历要求
    jobxingzhi = scrapy.Field() # 岗位性质
    meihzouxiuxi = scrapy.Field() #每周休息
    salary = scrapy.Field() #薪酬范围
    fabushijian = scrapy.Field() #	发布时间
    chengnuoyueyin = scrapy.Field() #承诺月薪
    gongzuodidian = scrapy.Field() #工作地点
    xinzidaiyu = scrapy.Field() # 薪资待遇
    jobyaoqiu = scrapy.Field() #职位要求

    companyName = scrapy.Field() # 公司名字
    fZeRen = scrapy.Field() #负责人
    qq = scrapy.Field() # qq
    phone = scrapy.Field() # 电话
    mailBox = scrapy.Field() # 邮箱
    vx = scrapy.Field() # 微信
    Location = scrapy.Field() # 位置
    transit = scrapy.Field() # 公交