# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import pymysql
# import requests
from scrapy.pipelines.images import ImagesPipeline
import scrapy
# class TuPipeline2:
#     def __init__(self):
#         # 连接MySQL数据库
#         self.connect=pymysql.connect(host='localhost',user='root',password='liuhonga',db='img',port=3306)
#         self.cursor=self.connect.cursor()
#     def process_item(self, item, spider):
#         # 往数据库里面写入数据
#         self.cursor.execute('insert into img1(url,_image)VALUES ("{}","{}")'.format(item['image_urls'],item['images']))
#         self.connect.commit()
#     # 关闭数据库
#     def close_spider(self,spider):
#         self.cursor.close()
#         self.connect.close()
   
# class TuPipeline1:
#     def process_item(self, item, spider):
#         url = item['image_urls']
#         name=item["images"]
#         path = '/Users/bgcde/文档/jpg/laj/' #路径自行设定
#         # print(name)
#         dizi=path + name
#         data = requests.get(url)
#         print(dizi)
#         # with open(dizi, 'wb') as file:
#         #     file.write(data.content)
#         #     file.flush()
#         return item

class TuPipeline(ImagesPipeline):
        def get_medie_requests(self,item,info):
            image_link = item['image_link']
            print(image_link)
            yield scrapy.Request(image_link)
        def item_completed(self,results,item,info):
            return item
