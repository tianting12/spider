# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QcwyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    salary = scrapy.Field()
    education = scrapy.Field()
    workExperience = scrapy.Field()
    needNumPeople = scrapy.Field()
    workAddress = scrapy.Field()
    company = scrapy.Field()
    companyType = scrapy.Field()
    companySize = scrapy.Field()
    companyIndustry = scrapy.Field()
    fuli = scrapy.Field()
    description = scrapy.Field()
    jobRequire = scrapy.Field()
    jobUrl = scrapy.Field()


