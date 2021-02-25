# import requests
# import re
# import pymysql
# import time
# from bs4 import BeautifulSoup 
# '''
# 总思路：
# 0.在”https://wallhaven.cc/toplist“加“?page=页数”可进行翻页
# 1.使用Chrome开发工具，发现在主页有两种图片的url，一个为缩略图可直接下载，一个为原图，需要进入下载。此次选择下载原图。
# 2.观察网页源代码，原图url在<a class="perview">中，使用BeautifulSoup和正则表达式获取ID。
# 3.获取ID后进入单图片页面，发现有3个带有<img>标签的片段，其中第三个片段的src为图片下载url。
# 4.获取下载url后便可下载到制定文件夹中。
# '''

# '''
# 函数说明：
# getPic_ID()：获取每张图的ID
# getPic_HTML()：获取每张图的url
# Download():根据url下载并保存图片
# '''

def getPic_ID(pic_id, page, header):
    url = "https://wallhaven.cc/search?q=id%3A5&categories=111&purity=110&ratios=16x9&sorting=relevance&order=desc&page="+str(page) 
    
    r = requests.get(url = url,headers = header,verify = False)
    soup = BeautifulSoup(r.text, 'html.parser')
    for tag in soup.find_all("a",class_="preview"):
        picURL = re.findall('href="https://wallhaven.cc/w/(.*?)"',str(tag))
        pic_id.append(picURL[0]) #findall元素问列表，我们的目的是存储str类型的id
    print(pic_id)
    return pic_id
    
def getPic_HTML(picHTML, pic_id, page, header):
    for i in range(len(pic_id)):
        pic_url2='https://wallhaven.cc/full/'+pic_id[i]
        try:
            r = requests.get(url = pic_url2, headers = header,verify = False)
            #print(r.text)
            soup = BeautifulSoup(r.text, 'html.parser')
            items = soup.find_all('img')
            picHTML.append(items[2].attrs['src']) #第3个<img>是可下载的url
            print("第"+str(page)+"页第"+str(i)+"张图片url获取成功")
        except:
            print("第"+str(page)+"页第"+str(i)+"张图片url获取失败")
    
#    for i in range(len(picHTML)):
#        print(picHTML[i])
    return picHTML

def Download(picHTML, page):
    path = '/Users/bgcde/文档/blog的副本/jpg/laj' #路径自行设定
    for i in range(len(picHTML)):
        html = picHTML[i]
        img_name = path + str(page)+"-"+str(i)+'.png' #图片名称
            data = requests.get(picHTML[i])
            with open(img_name, 'wb') as file:
                file.write(data.content)
                file.flush()
    
def main():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        }
    for page in range(1,70):#此为1~5页，自行设定
        pic_id = [] #每张图片的id列表
        picHTML = [] #每张图片的下载url列表
        getPic_ID(pic_id, page, header)
        getPic_HTML(picHTML, pic_id, page, header)
        Download(picHTML, page)
    
main()



# https://w.wallhaven.cc/full/vg/wallhaven-vgrwe8.jpg