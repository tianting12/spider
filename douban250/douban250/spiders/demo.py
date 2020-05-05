#_*_coding:utf-8_*_
#作者       ：  Deth
#创建时间    : 2020/5/5 14:41
#文件       ： demo. py
# IDE       : PyCharm
import re

import requests
from lxml import etree

import requests

cookies = {
    'ASP.NET_SessionId': 'bedl2acor0m4shwuagrc3y5q',
    'ASPSESSIONIDSACCDABC': 'NEBHHFBACABDFDBKLHKDGNNH',
    '__utma': '128509784.831923733.1588660506.1588660506.1588660506.1',
    '__utmc': '128509784',
    '__utmz': '128509784.1588660506.1.1.utmcsr=(direct)^|utmccn=(direct)^|utmcmd=(none)',
    '__utmt': '1',
    '__utmb': '128509784.20.10.1588660506',
    'VisitNum': '15',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Referer': 'http://eps.xcmg.com:90/custom/GroupNewsList.aspx?GroupId=141^&child=true',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('pagetype', 'GroupNewsList^'),
    ('keyword', '^'),
    ('GroupId', '141^'),
    ('buyGroupId', '^'),
    ('companyId', '^'),
    ('child', 'true^'),
    ('p', '145'),
)

r = requests.get('http://eps.xcmg.com:90/custom/GetNewsPageData.aspx?pagetype=GroupNewsList&keyword=&GroupId=141&buyGroupId=&companyId=&child=true&p=145', headers=headers,cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://eps.xcmg.com:90/custom/GetNewsPageData.aspx?pagetype=GroupNewsList^&keyword=^&GroupId=141^&buyGroupId=^&companyId=^&child=true^&p=145', headers=headers, cookies=cookies, verify=False)

if r.status_code == 200:
    r.encoding =r.apparent_encoding
    print(r.text)
    print(r)
#
data = etree.HTML(r.text)
print(data)
print(len(data.xpath('//ul[@class="mainbox"]/li')))
for li in data.xpath('//ul[@class="mainbox"]/li'):
    time = li.xpath('./div/text()')[0]
    href = li.xpath('./a/@href')[0]

    num = re.search((("(\d+)")),href).group(1)
    href ='http://eps.xcmg.com:90/custom/News/ViewNews.aspx?id=' +num
    title = li.xpath('./a/text()')[0]
    print(time,title,href)


name = '麦家 / 北京十月文艺出版社 / 2019-4 / 55.00元'
print(name.split('/'))

print([f'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={20 * i}&type=T' for i in range(25)])