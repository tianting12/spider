知乎spider

####安装准备####

环境需求：python3.6+

安装scrapy

#shell

pip install -i scrapy  https://pypi.douban.com/simple

### 配置数据库参数

进入文件夹zhihu

找到settings.py文件，拉到最后配置mysql和redis信息进行配置为自己的
可以自己通过修改pipelines进行存储方式的改变，
然后通过注释和取消注释ITEM_PIPELINES里的相关信息可实现开启mysql的存储方式


####settings配置 断点续爬
文件夹scrapy_redis 进行断点续爬的文件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #定义一个去重的类，用来将url去重
SCHEDULER = "scrapy_redis.scheduler.Scheduler"   #指定队列
SCHEDULER_PERSIST = True  #将程序持久化保存

mysql数据库，请执行使用以下sql语句创建数据表

```mysql
create table zhihu
(
    answer_count    int          null comment '回答数量',
    articles_count  int          null comment '写过的文章数',
    follower_count  int          null comment '粉丝数量',
    following_count int          null comment '关注了多少人',
    educations      varchar(255) null comment '教育背景',
    description     varchar(255) null comment '个人描述',
    locations       varchar(50)  null comment '所在地',
    url_token       varchar(255) not null comment '知乎给予的每个人用户主页唯一的ID'
        primary key,
    name            varchar(50)  null comment '用户昵称',
    employments     varchar(50)  null comment '工作信息',
    business        varchar(50)  null comment '一些工作或者商业信息的合集',
    user_type       varchar(50)  null comment '用户类型，可以是个人，也可以是团体等等',
    headline        varchar(255) null comment '个人主页的标签',
    voteup_count    int          null comment '获得的赞数',
    thanked_count   int          null comment '获得的感谢数',
    favorited_count int          null comment '被收藏次数'
);

```
注意表名要和settings.py文件里面的相对应，这里默认是`zhihu`

知乎数据接口

 # 这个是查询粉丝或者关注列表里面的用户需要附带的参数
include_follow = 'data[*].answer_count, articles_count, gender, follower_count, is_followed, is_following, badge[?(type = best_answerer)].topics'

# 这个是查询个人信息需要附带的一个参数
include_userinfo = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'

# 获取粉丝列表的url,里面的参数分别是用户的ID，查询参数，这个在浏览器复制就可以了，offset表示第几页的粉丝或者关注者，limit表示每页的数量，这里网页上默认是20  
followers_url = 'https://www.zhihu.com/api/v4/members/{user_name}/followers?include={include_follow}&offset={offset}&limit={limit}'


# 获取关注列表的URL，根上面的就差了一个字母
followees_url = 'https://www.zhihu.com/api/v4/members/{user_name}/followees?include={include_follow}&offset={offset}&limit={limit}'
   
#获取用户个人信息的URL 参数user_name 用户唯一标识符  include_userinfo 个人信息的参数
userinfo_url = 'https://www.zhihu.com/api/v4/members/{user_name}?include={include_userinfo}'

本次用到一个ip池用来随机更换ip








