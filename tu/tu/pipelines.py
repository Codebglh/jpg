# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class TuPipeline:
    def __init__(self):
        # 连接MySQL数据库
        self.connect=pymysql.connect(host='localhost',user='root',password='liuhonga',db='img',port=3306)
        self.cursor=self.connect.cursor()
    def process_item(self, item, spider):
        # 往数据库里面写入数据
        self.cursor.execute('insert into img(url,_image)VALUES ("{}","{}")'.format(item['image_urls'],item['images']))
        self.connect.commit()
    # 关闭数据库
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
   
class TUipeline1:
    def process_item(self, item, spider):
        url = item['image_urls']
        name=item["images"]
        path = '/Users/bgcde/文档/jpg/laj' #路径自行设定
        print(url)
        print(name)
        return item
        
        # for i in range(len(picHTML)):
        #     html = picHTML[i]
        #     img_name = path + str(page)+"-"+str(i)+'.png' #图片名称
        #         data = requests.get(picHTML[i])
        #         with open(img_name, 'wb') as file:
        #             file.write(data.content)
        #             file.flush()    
        #             return item