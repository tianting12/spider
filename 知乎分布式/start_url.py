import redis

from zhihu.settings import *





pool_redis = redis.ConnectionPool(host=str(REDIS_HOST), port=REDIS_PORT, password=REDIS_PARAMS['password'],
                                  decode_responses=True,)

r = redis.Redis(connection_pool=pool_redis)
url = 'https://www.zhihu.com/api/v4/members/ponyma/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
r.lpush('zhihu:start_urls', url)

