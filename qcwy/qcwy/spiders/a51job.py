# -*- coding: utf-8 -*-
import re
import scrapy
from qcwy.items import QcwyItem


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['51job.com']

    def start_requests(self):
        citys = ['070200']
        queryes = ['python']
        for city in citys:
            for query in queryes:
                    url = f'https://search.51job.com/list/{city},000000,0000,00,9,99,{query},2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
                    yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        infoes = response.xpath('//*[@id="resultList"]/div/p/span/a/@href').getall()
        for info in infoes:

            yield scrapy.Request(url=info,callback=self.second_parse)

        next_url = response.xpath('//div[@class="p_in"]/ul/li[last()]/a/@href').get()
        print(next_url)
        if next_url:
            print(next_url)
            yield scrapy.Request(url= next_url,callback=self.parse)

    def second_parse(self,response):
        item = QcwyItem()
        #工作名字
        item['jobName'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/@title').get()
        #薪资
        item['salary'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()').get()
        #教育程度
        item['education'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/@title').re('(本科|[硕博]士|大专|在校生/应届生)') \
            if  response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/@title').re('(本科|[硕博]士|大专|在校生/应届生)') else '无要求'
        #工作经验
        item['workExperience'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/@title').re('(\d-\d年经验|\d年经验)') \
            if  response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/@title').re('(\d-\d年经验|\d年经验)') else '无要求'
        #需要几人
        item['needNumPeople'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/@title').re('(招\d人)') \
            if  response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/@title').re('(招\d人)') else '无要求'
        #福利待遇
        item['fuli'] = '||'.join(response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/div/div/span/text()').getall())
        #公司名字
        item['company'] = response.xpath('/html/body/div[3]/div[2]/div[4]/div[1]/div[1]/a/p/@title').get()
        #公司类型
        item['companyType'] = response.xpath('/html/body/div[3]/div[2]/div[4]/div[1]/div[2]/p[1]/text()').get()
        #公司规模
        item['companySize'] = response.xpath('/html/body/div[3]/div[2]/div[4]/div[1]/div[2]/p[2]/text()').get()
        #公司行业
        item['companyIndustry'] = response.xpath('/html/body/div[3]/div[2]/div[4]/div[1]/div[2]/p[3]/@title').get()
        #上班地址
        item['workAddress'] = response.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()').get()
        #职位描述
        desc = '\n'.join([i.strip() for i in response.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/p/text()').getall()[:-6] if '\r\n' not in i])
        key = re.findall('\S\S要求', desc)
        print(desc)
        if not key:
            key = '任职资格'
        else:
            key = key[0]
        if key not in desc:
            item['description'] = desc
            item['jobRequire'] = desc
        else:
            item['description'] = desc.split(key)[0]
            # 任职要求
            item['jobRequire'] = desc.split(key)[1]

        #职位链接
        item['jobUrl'] =response.url
        yield item
