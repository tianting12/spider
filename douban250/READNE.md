豆瓣小说spider
网址  https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=0&type=T

需求 爬取 书名， 作者，评分，多少人评论，简介，图片url ，并下载图片在本地

准备

##环境 python 3.6++
scrapy，pymongo

pip install -i scrapy https://pypi.douban.com/simple

pip install -i pymongo https://pypi.douban.com/simple

###修改setting Mongodb配置按照自己的来

IMAGES_STORE = 'images'  可以设置自己想保存的路径

关于ImagesPipeline
需要在item里面有两个字段一个是image_urls一个是image
image_urls 需要下载的连接，image是下载一个一个详情

[(True,
  {'checksum': '2b00042f7481c7b056c4b410d28f33cf',
   'path': 'full/0a79c461a4062ac383dc4fade7bc09f1384a3910.jpg',
   'url': 'http://www.example.com/files/product1.pdf'}),
 (False,
  Failure(...))]
meta 将name传入进行，从而进行自定义一个name名字
 def get_media_requests(self,item,info):
        for image_url in item['image_url']:
            yield scrapy.Request(image_url, meta={"name":item['book_name']})

用来进行检查是否下载成功没成功则删除
def item_completed(self,results,item,info):
        image_paths = [x['path'] for ok, x in results if ok] # ok判断是否下载成功
        if not image_paths:
            raise DropItem('Item contains no images')
	
        return item

#用来自定义图片名字
 def file_path(self,request,response=None,info=None):

        filename = request.meta['name'] +'.jpg'
        return filename
