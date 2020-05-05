#_*_coding:utf-8_*_
#作者       ：  Deth
#创建时间    : 2020/4/16 20:23
#文件       ： demo. py
# IDE       : PyCharm
import csv
import re
import time

from  multiprocessing import Pool,Lock
import requests
from lxml import etree


def get_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36(KHTML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.36', #头部信息\
        'Referer':'https://m.fang.com/esf/xian/',
    }

    html = requests.get(url).text
    # re提取url参数部分，并拼接出url
    real_url = re.findall(r'//location.href="(.*?)";', html)[0]
    print('real_url:', real_url)
    text = requests.get(url=real_url)

    text.encoding = text.apparent_encoding
    infoes = etree.HTML(text.text).xpath('//dl[@class="clearfix"]')
    item = {}
    for info in infoes:
        try:
            item['title'] = info.xpath('./dd/h4/a/span/text()')[0]

            dataes = info.xpath('.//p[@class="tel_shop"]/text()')
            dataes = list(map(lambda x: re.sub(r"\s", "", x), dataes))

            for house in dataes:

                if '室' in house:
                    item["house_size"] = house
                elif '层' in house:
                    item["house_louceng"] = house
                elif '向' in house:
                    item["house_chaoxiang"] = house
                elif '�O' in house:
                    item['house_area'] = re.match('(\d+)',house).group(1) + '㎡'
            # item['house_size'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[0].strip()
            # item['house_area'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[1].strip()
            # item['house_louceng'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[2].strip()
            # item['house_chaoxiang'] = info.xpath('./dd/p[@class="tel_shop"]/text()').extract()[3].strip()
            item['xiaoqu'] = info.xpath('//p[@class="add_shop"]/a/text()')[0].strip()
            item['weizhi'] = info.xpath('//p[@class="add_shop"]/span/text()')[0]
            price_s = info.xpath('.//dd[@class="price_right"]/span/b/text()')[0]
            price_w = info.xpath('.//dd[@class="price_right"]/span[1]/text()')[0]
            print(item)
            if price_s and price_w:
                item['price'] = ''.join(price_s) + ''.join(price_w)
            else:
                item['price'] = '暂无数据'
            pricemi = info.xpath('.//dd[@class="price_right"]/span[2]/text()')[0]
            item['pricemi'] = re.match('(\d+)',pricemi).group(1) + '㎡'
        except:
            pass
        lock = Lock()
        lock.acquire()
        print(item)
        with open('xian.csv', 'a+', encoding='utf-8', newline='') as f:
            csvWriter= csv.writer(f)
            date = [
                item.get('title', ''),
                item.get('house_size', ''),
                item.get('house_area', ''),
                item.get('house_louceng', ''),
                item.get('house_chaoxiang', ''),
                item.get('xiaoqu', ''),
                item.get('weizhi', ''),
                item.get('price', ''),
                item.get('pricemi', ''),
            ]
            csvWriter.writerow(date)
        lock.release()

if __name__ == '__main__':
    num = int(input('请输入要爬取的页数'))
    city = input('请输入要爬取的城市')
    std = time.time()
    f = open(f'{city}.csv','w',encoding='utf-8',newline='')
    csvWriter1 = csv.writer(f)
    csvWriter1.writerow(['标题','规格','面积','楼层','朝向','小区','位置','总价','价钱'])
    # for i in range(1,num+1):  #1241.0658843517303  395.5638921260834
    #     print('{0:*^50}'.format('*'))
    #     print(f'开始爬取第{i}页')
    #     url = f'https://{city}.esf.fang.com/house/i3{i}/'
    #     print(f'第{i}页爬取结束')
    #     get_info(url)
    pool = Pool()
    urls = [f'https://{city}.esf.fang.com/house/i3{i}/' for i in range(1,num+1)]
    pool.map(get_info,urls)
    end = time.time()
    print(f'花费时间是{end - std}')