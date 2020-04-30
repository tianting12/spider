# #_*_coding:utf-8_*_
# #作者       ：  Deth
# #创建时间    : 2020/4/16 15:21
# #文件       ： demo. py
# # IDE       : PyCharm
# import re
#
# import requests
# from lxml import etree
#
# def get_redirect_url(url):
#     # 重定向前的链接
#
#     # 请求头，这里我设置了浏览器代理
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#     # 请求网页
#     response = requests.get(url)
#
#     html = requests.get(response.url).text
#
#     real_url = url + '?' + re.findall(r't2=\'(.*?)\'', html)[0]
#     print(real_url)
#     r = requests.get(url=real_url,headers=headers).text
#     # print(r)
#     response = etree.HTML(r)
#     item={}
#     for info in response.xpath('//dl[@class="clearfix"]'):
#
#         item['title'] = info.xpath('./dd/h4/a/span/text()').get()
#         infoes = info.xpath('.//p[@class="tel_shop"]/text()').getall()
#         infoes = list(map(lambda x: re.sub(r"\s", "", x), infoes))
#         for house in infoes:
#
#             if '室' in house:
#                 item["house_size"] = house
#             elif '层' in house:
#                 item["house_louceng"] = house
#             elif '向' in house:
#                 item["house_chaoxiang"] = house
#             elif '㎡' in house:
#                 item['house_area'] = house
#
#         # item['house_size'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[0].strip()
#         # item['house_area'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[1].strip()
#         # item['house_louceng'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[2].strip()
#         # item['house_chaoxiang'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[3].strip()
#         item['xiaoqu'] = info.xpath('//p[@class="add_shop"]/a/text()').extract()[0].strip()
#         item['weizhi'] = info.xpath('//p[@class="add_shop"]/span/text()').extract()[0]
#         price_s = info.xpath('.//dd[@class="price_right"]/span/b/text()').get()
#         price_w = info.xpath('.//dd[@class="price_right"]/span[1]/text()').get()
#         if price_s and price_w:
#             item['price'] = ''.join(price_s) + ''.join(price_w)
#         else:
#             item['price'] = '暂无数据'
#         print(item)
#
# # 'rfss=1-bc942aaa1482bcc67d-52'
# if __name__ == '__main__':
#     url = 'https://xian.esf.fang.com/house/i31'
#     get_redirect_url(url)

import requests
import re
from lxml import etree

start_url = 'https://xian.esf.fang.com/house/i33/'
html = requests.get(start_url).text
# re提取url参数部分，并拼接出url
real_url = re.findall(r'//location.href="(.*?)";', html)[0]
print('real_url:', real_url)
r = requests.get(url=real_url).text
print(r)
