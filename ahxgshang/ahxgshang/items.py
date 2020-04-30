# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AhxgshangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  #企业名称
    ID = scrapy.Field() # 统一社会信用代码/工商注册号
    registeredAddress = scrapy.Field() #注册地址
    registeredTime = scrapy.Field() #注册日期
    legalPerson = scrapy.Field() #法定代表人
    businessScope = scrapy.Field() #经营范围
    area = scrapy.Field() #地区
    city = scrapy.Field() #县市
    category = scrapy.Field() #分类
    companyType = scrapy.Field() #企业类型
    companyStatus = scrapy.Field() #公司现状

    A = ['企业名称','统一社会信用代码/工商注册号','注册地址','注册日期','法定代表人','经营范围','地区','县市','分类','企业类型','公司现状',]