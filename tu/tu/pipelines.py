# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
# import pymysql
# import requests
# from scrapy.pipelines.images import ImagesPipeline
import pymysql
import scrapy
# class TuPipeline:
#     def __init__(self):
#         # 连接MySQL数据库
#         self.connect=pymysql.connect(host='127.0.0.1',user='root',password='liuhonga',db='liu',port=3306)
#         self.cursor=self.connect.cursor()
#     def process_item(self, item, spider):
#         # 往数据库里面写入数据
#         self.cursor.execute('insert into img(url,img)VALUES ("{}","{}")'.format(item['urls'],item['images']))
#         self.connect.commit()
#     # 关闭数据库
#     def close_spider(self,spider):
#         self.cursor.close()
#         self.connect.close()
   
