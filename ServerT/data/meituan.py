import csv
import requests
import json


def anmo():
    url = 'https://sh.meituan.com/ptapi/recommends?limit=100'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
    response=requests.get(url, headers=headers, verify=False)
    datas = json.loads(response.text)
    print(len(datas))
    for data in datas:
        title = data['title']  # 名字
        lowprice = data['lowPrice']  # 最低价
        avgprice = data['avgPrice']  # 平均价格
        score = data['score']
        areaname = data['areaName']
        result = [title, areaname, lowprice, avgprice,score]
        with open('1.csv', 'a+', newline='', encoding='gb18030') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(result)


if __name__ == '__main__':

    anmo()


