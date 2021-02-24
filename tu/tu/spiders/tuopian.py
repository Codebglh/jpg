import scrapy
from tu.items import TuItem

class TuopianSpider(scrapy.Spider):
    name = 'tuopian'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['https://wallhaven.cc/search?q=id%3A5&categories=111&purity=110&ratios=16x9&sorting=relevance&order=desc&page={a}' for a in range(0,1000)]
    
    def parse(self, response):
        y = response.xpath('/html/body/main/div/section/ul')
        for i in y:
            k=i.xpath('./li/figure/@data-wallpaper-id').extract()
            o=len(k)
            # print(i)
            for x in range(o):
                a=k[x]
                qian=a[0:2]
                url="https://w.wallhaven.cc/full/"+qian+"/wallhaven-"+a+".jpg"
                img="6833939bly1gici"+a+"j20zk0m8"+a[0:3]+".jpg"
                item = TuItem()
                item["image_urls"]=url
                item["images"]=img
                print(img)
                # print(qian)
                # print(url)
                yield item