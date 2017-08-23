from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv
import re
from time import sleep

# csv_file = open("rent.csv", "r")
# csv_reader = csv.reader(csv_file, delimiter=',')
#
# for row in csv_reader:
#     if '西乡' in row:
#         print(row[0])
#
# csv_file.close()
# print('finish')
# sleep(10000)

money_pattern = re.compile(r'<b>(%d*)<\/b>')
csv_file = open("rent.csv", "w")
csv_writer = csv.writer(csv_file, delimiter=',')
PAGE = 1
times = 0

url = 'http://bj.58.com/pinpaigongyu/pn/{page}/'

while True:
    print("fetch:", url.format(page=PAGE))
    response = requests.get(url.format(page=PAGE), verify=False)
    html = BeautifulSoup(response.text, "html.parser")
    house_list = html.select(".list > li")

    if not house_list:
        times += 1
        if times < 3:
            print('sleep 4 restart : ', times)
            sleep(4)
            continue
        else:
            print('finish!!!!!!!')
        break
    times = 0
    PAGE += 1
    for house in house_list:
        value = house.select('div')
        house_money = house.select(".money")[0].select("b")[0]
        money = re.findall("\d+", str(house_money))
        house_name = house.select('.des')[0].select('h2')[0].string
        house_info_list = house_name.split()
        house_url = urljoin(url, house.select("a")[0]["href"])

        if '公寓' in house_info_list[1]:
            location = house_info_list[0]
        else:
            location = house_info_list[1]
        csv_writer.writerow([house_name, location, money, house_url])

csv_file.close()















