# -*- coding: utf-8 -*-

# Scrapy settings for tt project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tt'

SPIDER_MODULES = ['tt.spiders']
NEWSPIDER_MODULE = 'tt.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'referer': 'https://www.tntsupermarket.com/delivery-to-home/snacks.html',
   'cookie': 'mage-translation-storage=%7B%7D; mage-translation-file-version=%7B%7D; form_key=WKGpyCaItcm2S6OX; _ga=GA1.2.1927541043.1584646609; __zlcmid=xIizrGqp90e9SQ; mage-messages=; _gid=GA1.2.19083644.1585538020; location=Surrey%2C%20BC%2C%20V4P%200A6; province=BC; preferedstorecode=RA; jjSPnsABk=AmAVbylxAQAAUd_mbLE1d1e115DnXQcK_OGkQJGa5WeVLVrwvgAAAXEpbxVgAbScEIY|1|0|3a0887cd74db6138cc35f03c9316c31f2a1178e1; PHPSESSID=2kkuj90ovemv2io1o1oe76vl8g; form_key=WKGpyCaItcm2S6OX; mage-cache-sessid=true; store_cn=2kkuj90ovemv2io1o1oe76vl8g; private_content_version=9cd0a86388d4d67e093c9cac03133a53; RT="z=1&dm=tntsupermarket.com&si=ywngm5rhhb&ss=k8dwectn&sl=0&tt=0"; section_data_ids=%7B%22cart%22%3A1585714176%2C%22directory-data%22%3A1585714176%2C%22customer%22%3A1585714176%2C%22compare-products%22%3A1585714176%2C%22last-ordered-items%22%3A1585714176%2C%22captcha%22%3A1585714176%2C%22wishlist%22%3A1585714176%2C%22instant-purchase%22%3A1585714176%2C%22multiplewishlist%22%3A1585714176%2C%22persistent%22%3A1585714176%2C%22review%22%3A1585714176%2C%22recently_viewed_product%22%3A1585714176%2C%22recently_compared_product%22%3A1585714176%2C%22product_data_storage%22%3A1585714176%2C%22paypal-billing-agreement%22%3A1585714176%2C%22checkout-fields%22%3A1585714176%2C%22collection-point-result%22%3A1585714176%2C%22pickup-location-result%22%3A1585714176%7D'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'tt.middlewares.TtSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'tt.middlewares.TtDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tt.pipelines.TtPipeline': 300,
    'tt.pipelines.TtImagesPipeline': 302,
}
IMAGES_STORE = 'images'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 2
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
