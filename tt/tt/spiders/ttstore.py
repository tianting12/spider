# -*- coding: utf-8 -*-
import scrapy
from tt.items import TtItem
from copy import deepcopy

class TtstoreSpider(scrapy.Spider):
    name = 'ttstore'
    allowed_domains = ['tntsupermarket.com']
    start_urls = ['https://www.tntsupermarket.com/delivery-to-home/snacks.html']

    def parse(self, response):
        # 大分类分组
        li_list = response.xpath("//*[@id='maincontent']/div/div[2]/div[1]/ul")
        for li in li_list:
            item = TtItem()
            item["b_cate"] = li.xpath("./li/a/text()").extract_first()

            # 小分类分组
            a_list = response.xpath("//*[@id='narrow-by-list']/div[1]/div[2]/ol/li")
            for a in a_list:
                item["s_cate"] = a.xpath("./a/span/text()").extract_first()
                item["s_href"] = a.xpath("./a/@href").extract_first()
                yield scrapy.Request(
                    item["s_href"],
                    callback=self.parse_cart_list,
                    meta={"item":item}
                )
    def parse_cart_list(self,response):
        # 产品列表页
        item = deepcopy(response.meta["item"])
        cart_list = response.xpath("//*[@id='layer-product-list']/div[2]/ol/li")
        for cart in cart_list:
            item["name"] = cart.xpath("./div/div/strong/a/text()").extract_first()
            item["href"] = cart.xpath("./div/div/strong/a/@href").extract_first()
            item["final_price"] = cart.xpath("//span[@class='price-container price-final_price tax weee']/span/span/text()").extract_first()
            item["was_price"] = cart.xpath("//*[@class='was-price']").extract_first()
            # item["image_urls"] = cart.xpath("//div[@class='product-item-info']//span/img/@src").extract()
            item["image_url"] = cart.xpath("./div/a/span/span/img/@src").extract()
            yield scrapy.Request(
                item["href"],
                callback=self.parse_cart_detail,
                meta={"item":deepcopy(item)}
            )

        netx_url = response.xpath("//li[@class='item pages-item-next']/a/@href").extract_first()

        if netx_url:
            yield scrapy.Request(
                netx_url,
                callback=self.parse_cart_list,
                meta={"item":item}
            )

    def parse_cart_detail(self,response):
        item = response.meta["item"]
        item["size"] = response.xpath("//div[@class='swatch-option selected']/text()").extract_first()
        item["cart_galley_small_img"] = response.xpath("//*[@class='fotorama__nav__shaft']//img/@src").extract()
        item["cart_content_img"] = response.xpath("//div[@class='value']//img/@src").extract()
        item["was_price"] = response.xpath("//span[@class='was-price notes']/span/span").extract_first()

        yield item


