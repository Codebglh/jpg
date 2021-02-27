import pymysql
import requests
from fake_useragent import UserAgent  # 导入包
conn = pymysql.connect(host="127.0.0.1", user="root",password="liuhonga",database="liu",charset="utf8")
cursor = conn.cursor()
sql = "SELECT url ,img from img;"
cursor.execute(sql)
suju = cursor.fetchall()
cursor.close()
conn.close()
for x in range(0,len(suju)):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    c=suju[x]
    for y in range(0,1):
        name=c[1]
        url=c[0]
        path = 'laj/'+name        
        data = requests.get(url,headers=headers)
        with open(path, 'wb') as file:
            file.write(data.content)
            # file.flush()
            print(name)
