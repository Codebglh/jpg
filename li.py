import pymysql
import requests

def main():
    conn = pymysql.connect(host="localhost", user="root",password="liuhonga",database="img",charset="utf8")
    cursor = conn.cursor()
    sql = "SELECT url ,_image from img;"
    cursor.execute(sql)
    suju = cursor.fetchall()
    cursor.close()
    conn.close()
    for x in range(0,len(suju)):
        c=suju[x]
        for y in range(0,1):
            name=c[1]
            url=c[0]
            # print(url)
            print(name)
            path = '/Users/bgcde/文档/jpg/laj/' 
            dizi=path + name
            data = requests.get(url)
            with open(dizi, 'wb') as file:
                file.write(data.content)
                file.flush()
main()