# -*- coding: utf-8 -*-
import copy
import re

import scrapy
import json

from weibo.items import WeiboItem


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['m.weibo.cn']
    WEIBO_USER_CONFIG = {
        'BASE_URL': 'https://m.weibo.cn',
        'USERS_UID': ['6041482474','3052026964','3886728711','5848118257','6817248303','6176350049'],
        'TEXT_ALL':'https://m.weibo.cn/api/container/getIndex?containerid=230413{}_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page={}',#某一个人的文章参数containerid page
        'TEXT_URL':'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id_type=0', #微博说说 参数mid 文章表题
        'USER_UID':'https://m.weibo.cn/api/container/getIndex?uid={}&type=uid&value={}', # 获取containerid 参数 uid 个人信息
        'USER_CONTAINERID':'https://m.weibo.cn/api/container/getIndex?containerid={}_-_INFO&title=%E5%9F%BA%E6%9C%AC%E8%B5%84%E6%96%99&luicode=10000011&lfid={}', #获取个人信息参数 containerid
        'USER_INFO':'https://m.weibo.cn/api/container/getIndex?type=uid&value={}'#获取个人信息参数uid
    }


    def start_requests(self):

        for uid in self.WEIBO_USER_CONFIG['USERS_UID']:
            url = self.WEIBO_USER_CONFIG['TEXT_ALL'].format(uid,1)
            # print(url)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        data = json.loads(response.text)

        for i in data['data']['cards']:
            if i.get('mblog'):
                mid = i['mblog']['mid']

                text_url = self.WEIBO_USER_CONFIG['TEXT_URL'].format(mid,mid)
                yield  scrapy.Request(url=text_url,callback=self.getuid_parse,dont_filter=True)

        if data.get('data').get('cardlistInfo').get('page'):
            page = data['data']['cardlistInfo']['page']
            page_url = re.sub('page=\d+','page={}'.format(page),response.url)
            yield scrapy.Request(url=page_url,callback=self.parse)

    def getuid_parse(self,response):
        data = json.loads(response.text)
        if data.get('data'):
            # print(r1['data']['data'])
            for j in data['data']['data']:
                uid = re.search('uid=(\d+)', j['user']['profile_url']).group(1)
                user_containerid = self.WEIBO_USER_CONFIG['USER_UID'].format(uid,uid)
                yield scrapy.Request(url=user_containerid,callback=self.usercontainerid_parse)

    def usercontainerid_parse(self,response):
        item = WeiboItem()
        data = json.loads(response.text)['data']
        item['name'] = data['userInfo']['screen_name'] #昵称
        item['gender'] = '男' if data['userInfo']['gender'] == 'm' else '女'# 性别
        item['weiboshu'] = data['userInfo']['statuses_count'] # 发布的文章数
        item['weibodengji'] = data['userInfo']['mbrank'] # 微博等级
        item['fensishu'] = data['userInfo']['followers_count'] # 粉丝人数
        item['guanzhuzhe'] = data['userInfo']['follow_count'] # 关注人数

        containerid = data['tabsInfo']['tabs'][0]['containerid']

        userinfo_url = self.WEIBO_USER_CONFIG['USER_CONTAINERID'].format(containerid,containerid)
        yield scrapy.Request(url=userinfo_url,callback=self.userifno_parse,meta={'item':copy.deepcopy(item)})

    def userifno_parse(self,response):
        item = response.meta['item']
        data = json.loads(response.text)['data']['cards']
        for j in data[0]['card_group']:

            item['jianjie'] = j['item_content'] if j.get('item_name') == '简介' else ''
            item['chushengriqi'] = j['item_content'] if j.get('item_name') == '注册时间' else ''

        for i in data[1]['card_group']:
           item['chushengriqi'] = i['item_content'] if i.get('item_name') == '生日' else ''
           item['location'] = i['item_content'] if i.get('item_name') == '所在地' else ''
           item['xueli'] = i['item_content'] if i.get('item_name') == '大学' else ''

        yield item