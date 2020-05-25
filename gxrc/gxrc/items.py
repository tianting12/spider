# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class GxrcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = Field() #职位名称
    company = Field() #公司名称
    salary = Field()  # 薪资
    location = Field() #工作地点
    release_time = Field() #发布时间
    num = Field() # 人数
    education = Field() #学历
    experience = Field() #经验
    company_type = Field()  #性质

    contact = Field() # 联系人
    contact_phone = Field() #联系电话
    contact_mailbox = Field() # 联系邮箱
    contact_address = Field() # 联系地址
