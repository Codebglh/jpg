###### 1、安装scrapy框架

```python
pip install scrapy
```

###### 2、创建虚拟环境

```python
python -m venv ***#为名字
```

###### 3、创建一个爬虫框架

```python
scrapy startproject xxxx(项目名字)
```

###### 4、创建一个爬虫

```python
cd xxxx(项目名字)
scrapy genspider xxx（爬虫名字） xxx（网站域名）   #创建爬虫
```

###### 5、修改setting.py文件

```python
USER_AGENT = #请求头
LOG_LEVEL = "WARNING"#报错等级提高简单错误不显示
ROBOTSTXT_OBEY = False#是否遵守爬虫协议改为否(原因你懂的)
CONCURRENT_REQUESTS #一次允许的最大请求数
DOWNLOAD_DELAY = 3#设置下载延迟时间,因而使得爬虫更像是人的行为,避免IP被屏蔽
DOWNLOADER_MIDDLEWARES = {
   'xymtest.middlewares.XymtestDownloaderMiddleware': 543,
}#设置下载中间键
ITEM_PIPELINES = {
   'xymtest.pipelines.XymtestPipeline': 300,
}#设置管道
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'#取消最后几行的注释
```

###### 6、修改items.py文件

```python
url=scrapy.Field()
```

###### 7、修改pipelines.py文件

```python
下载文件
```

###### 8、编写爬虫文件

```python
import scrapy
from tu.items import TuItem
# import Request
class TSpider(scrapy.Spider):
    name = 't'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['https://wallhaven.cc/toplist?page={a}' for a in range(1,2)]

    def parse(self, response):
        y = response.xpath('//body/main/div/section/ul')
        for i in y:
            k=i.xpath('./li/figure/a/@href').extract()
            item = TuItem()
            item["url"]=k
            yield Request(k, meta={'item': item}, callback = self.parse1)

    def parse1(self,response):
        item = response.meta['item']
        y=response.xpath('//body/main/section/div/img/@src').extract()
        yield item
```

###### 9、安装xpath谷歌插件xpath语法

```python
https://chrome.google.com/webstore/detail/hgimnogjllphhhkhlmebbmlgjoejdpjl
```

###### 10、运行爬虫

```python
cd xxxx(项目名字)
scrapy crawl xx(爬虫名字)#运行爬虫
```

###### 11、请求头包

```python
pip install fake_useragent #安装包
from fake_useragent import UserAgent#导入包
s=UserAgent(verify_ssl=False).random#运用包

from fake_useragent import UserAgent # 版本 '0.1.11'
s=UserAgent(verify_ssl=False).random
print(s)

```

###### 11、二级访问链接

```python
class TSpider(scrapy.Spider):
    name = 't'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['https://wallhaven.cc/toplist?page={a}' for a in range(1,135)]

    def parse(self, response):
        y = response.xpath('//body/main/div/section/ul')
        for i in y:
            k=i.xpath('./li/figure/a/@href').extract()
            o=len(k)
            for x in range(o):
                a=k[x]   
                yield scrapy.Request(a, callback = self.parse_detail)

    def parse_detail(self,response):
        y=response.xpath('//body/main/section/div/img/@src').extract()
        item = TuItem()
        item["url"]=y
        yield item
```

###### 12、图片下载中间件自带settings.py，items.py

```python
ITEM_PIPELINES={
'scrapy.pipelines.images.ImagesPipeline':201
}
IMAGES_STORE=** #图片路径
```

###### 13、数据存到数据库

```python
class TuPipeline1:
    def __init__(self):
        # 连接MySQL数据库
        self.connect=pymysql.connect(host='127.0.0.1',user='root',password='liuhonga',db='tupian',port=3306)
        self.cursor=self.connect.cursor()
    def process_item(self, item, spider):
        # 往数据库里面写入数据
        self.cursor.execute('insert into tupian(tupian)VALUES ("{}")'.format(item['image_urls']))
        self.connect.commit()
    # 关闭数据库
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
```

