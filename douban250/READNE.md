����С˵spider
��ַ  https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=0&type=T

���� ��ȡ ������ ���ߣ����֣����������ۣ���飬ͼƬurl ��������ͼƬ�ڱ���

׼��

##���� python 3.6++
scrapy��pymongo

pip install -i scrapy https://pypi.douban.com/simple

pip install -i pymongo https://pypi.douban.com/simple

###�޸�setting Mongodb���ð����Լ�����

IMAGES_STORE = 'images'  ���������Լ��뱣���·��

����ImagesPipeline
��Ҫ��item�����������ֶ�һ����image_urlsһ����image
image_urls ��Ҫ���ص����ӣ�image������һ��һ������

[(True,
  {'checksum': '2b00042f7481c7b056c4b410d28f33cf',
   'path': 'full/0a79c461a4062ac383dc4fade7bc09f1384a3910.jpg',
   'url': 'http://www.example.com/files/product1.pdf'}),
 (False,
  Failure(...))]
meta ��name������У��Ӷ������Զ���һ��name����
 def get_media_requests(self,item,info):
        for image_url in item['image_url']:
            yield scrapy.Request(image_url, meta={"name":item['book_name']})

�������м���Ƿ����سɹ�û�ɹ���ɾ��
def item_completed(self,results,item,info):
        image_paths = [x['path'] for ok, x in results if ok] # ok�ж��Ƿ����سɹ�
        if not image_paths:
            raise DropItem('Item contains no images')
	
        return item

#�����Զ���ͼƬ����
 def file_path(self,request,response=None,info=None):

        filename = request.meta['name'] +'.jpg'
        return filename
