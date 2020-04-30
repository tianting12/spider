# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #昵称
    # name = scrapy.Field() #  1
    # #user_token
    # urlToken = scrapy.Field() #  2
    # #标签
    # headline = scrapy.Field()#  3
    # #性别
    # gender = scrapy.Field()##  4
    # #回答
    # answerCount = scrapy.Field()##  5
    # #文章数
    # articlesCount = scrapy.Field()##  6
    # #粉丝数
    # followerCount = scrapy.Field()##  7
    # #被关注数
    # followedCount = scrapy.Field() # 8
    # #url
    # userUrl = scrapy.Field() #  9
    #
    # #个人描述
    # description = scrapy.Field()#  10
    #
    # #提问
    # questionCount = scrapy.Field()#  11
    # #收藏
    # favoriteCount = scrapy.Field()#  12
    # #被收藏数
    # favoritedCount = scrapy.Field()#  13
    # #专栏数
    # columnsCount =scrapy.Field()#  14
    # #
    #
    # #现居地
    # locations = scrapy.Field() # 15
    # #职业
    # business = scrapy.Field() # 16
    #
    # #school
    # school = scrapy.Field() #19
    #
    # #赞同
    # voteupCount = scrapy.Field()#  17
    # #喜欢
    # thankedCount = scrapy.Field()#  18

    answer_count = scrapy.Field()  # 回答数量
    articles_count = scrapy.Field()  # 写过的文章数
    follower_count = scrapy.Field()  # 粉丝数量
    following_count = scrapy.Field()  # 关注了多少人
    educations = scrapy.Field()  # 教育背景
    description = scrapy.Field()  # 个人描述
    locations = scrapy.Field()  # 所在地
    url_token = scrapy.Field()  # 知乎给予的每个人用户主页唯一的ID
    name = scrapy.Field()  # 用户昵称
    employments = scrapy.Field()  # 工作信息
    business = scrapy.Field()  # 一些工作或者商业信息的合集
    user_type = scrapy.Field()  # 用户类型，可以是个人，也可以是团体等等
    headline = scrapy.Field()  # 个人主页的标签
    voteup_count = scrapy.Field()  # 获得的赞数
    thanked_count = scrapy.Field()  # 获得的感谢数
    favorited_count = scrapy.Field()  # 被收藏次数


