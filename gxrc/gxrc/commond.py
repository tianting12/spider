#_*_coding:utf-8_*_
#作者       ：  Deth
#创建时间    : 2020/5/21 14:50
#文件       ： commond. py
# IDE       : PyCharm
import requests
import base64
import os
'''
通用文字识别（高精度版）
'''
AppId = 18502209
API_Key = 'yfaVb7kBnHX2HbXCxsWZsgYb'
Secret_Key = 'uNhluTF0bXIKG3Cb3lG6EKFVfACpD6M4'

from aip import AipOcr

def wenzi(img):
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_Key + '&client_secret=' + Secret_Key
    response = requests.get(host)

    access_token = response.json()['access_token']
    # print(access_token)
    # request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate'

    params = {"image": img}

    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response.json()['words_result'][0]['words']