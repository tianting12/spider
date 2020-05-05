֪��spider

####��װ׼��####

��������python3.6+

��װscrapy

#shell

pip install -i scrapy  https://pypi.douban.com/simple

### �������ݿ����

�����ļ���zhihu

�ҵ�settings.py�ļ��������������mysql��redis��Ϣ��������Ϊ�Լ���
�����Լ�ͨ���޸�pipelines���д洢��ʽ�ĸı䣬
Ȼ��ͨ��ע�ͺ�ȡ��ע��ITEM_PIPELINES��������Ϣ��ʵ�ֿ���mysql�Ĵ洢��ʽ


####settings���� �ϵ�����
�ļ���scrapy_redis ���жϵ��������ļ�
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #����һ��ȥ�ص��࣬������urlȥ��
SCHEDULER = "scrapy_redis.scheduler.Scheduler"   #ָ������
SCHEDULER_PERSIST = True  #������־û�����

mysql���ݿ⣬��ִ��ʹ������sql��䴴�����ݱ�

```mysql
create table zhihu
(
    answer_count    int          null comment '�ش�����',
    articles_count  int          null comment 'д����������',
    follower_count  int          null comment '��˿����',
    following_count int          null comment '��ע�˶�����',
    educations      varchar(255) null comment '��������',
    description     varchar(255) null comment '��������',
    locations       varchar(50)  null comment '���ڵ�',
    url_token       varchar(255) not null comment '֪�������ÿ�����û���ҳΨһ��ID'
        primary key,
    name            varchar(50)  null comment '�û��ǳ�',
    employments     varchar(50)  null comment '������Ϣ',
    business        varchar(50)  null comment 'һЩ����������ҵ��Ϣ�ĺϼ�',
    user_type       varchar(50)  null comment '�û����ͣ������Ǹ��ˣ�Ҳ����������ȵ�',
    headline        varchar(255) null comment '������ҳ�ı�ǩ',
    voteup_count    int          null comment '��õ�����',
    thanked_count   int          null comment '��õĸ�л��',
    favorited_count int          null comment '���ղش���'
);

```
ע�����Ҫ��settings.py�ļ���������Ӧ������Ĭ����`zhihu`

֪�����ݽӿ�

 # ����ǲ�ѯ��˿���߹�ע�б�������û���Ҫ�����Ĳ���
include_follow = 'data[*].answer_count, articles_count, gender, follower_count, is_followed, is_following, badge[?(type = best_answerer)].topics'

# ����ǲ�ѯ������Ϣ��Ҫ������һ������
include_userinfo = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,avatar_hue,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'

# ��ȡ��˿�б��url,����Ĳ����ֱ����û���ID����ѯ�������������������ƾͿ����ˣ�offset��ʾ�ڼ�ҳ�ķ�˿���߹�ע�ߣ�limit��ʾÿҳ��������������ҳ��Ĭ����20  
followers_url = 'https://www.zhihu.com/api/v4/members/{user_name}/followers?include={include_follow}&offset={offset}&limit={limit}'


# ��ȡ��ע�б��URL��������ľͲ���һ����ĸ
followees_url = 'https://www.zhihu.com/api/v4/members/{user_name}/followees?include={include_follow}&offset={offset}&limit={limit}'
   
#��ȡ�û�������Ϣ��URL ����user_name �û�Ψһ��ʶ��  include_userinfo ������Ϣ�Ĳ���
userinfo_url = 'https://www.zhihu.com/api/v4/members/{user_name}?include={include_userinfo}'

�����õ�һ��ip�������������ip








