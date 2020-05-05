知乎spider

####安装准备####

环境需求：python3.6+

安装scrapy，pymongo

#shell

pip install -i scrapy  https://pypi.douban.com/simple

pip install -i pymongohttps://pypi.douban.com/simple

进入文件夹weibo

找到settings.py文件，拉到最后配置mongodb信息配置为自己的

可以自己通过修改pipelines进行存储方式的改变，
然后通过注释和取消注释ITEM_PIPELINES里的相关信息可实现开启pipelines更改的存储方式


weibo爬虫流程
网站 是微博 .cn的这个网站
目的
根据一个人的发布的所有文章获取到单个文章的评论人的信息 
昵称 简介 性别微博等级 微博数 粉丝数 关注者 年龄 地区 学习 行业

详情看xmind