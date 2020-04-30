#_*_coding:utf-8_*_
#作者       ：  Deth
#创建时间    : 2020/4/22 16:39
#文件       ： getJsonData. py
# IDE       : PyCharm
import requests
import json
from ast import literal_eval
#
# url = 'https://img.kq36.com.cn/js/json/AreaJson.js?v=20200413'
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Ap'
#             'pleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'}
#
# data = requests.get(url = url,headers = headers)
# # print(data.text[10:-4])
# data.encoding = data.apparent_encoding
# cityes = literal_eval(data.text[10:-4])
# print(type(cityes))
# a=[]
# for city in cityes:
#     item = {
#         'provinceid':city['ProID'],
#         'cityid':city['CityID'],
#         'areaid':city['AreaID'],
#         'AreaName':city['AreaName']
#     }
#     a.append(item)
# print(a)

item = {'companyName': '\r\n            乌鲁木齐市德康惠众中医门诊部有限公司\r\n            ',
 'companyUrl': '/jobs/2662029',
 'jobName': '中医医生',
 'jobUrl': '/job/1988051'}

print(item.get('companyName').strip())