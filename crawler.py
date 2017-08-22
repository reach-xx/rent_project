from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv
import re

money_pattern = re.compile(r'<b>(%d*)<\/b>')
csv_file = open("rent.csv", "w")
csv_writer = csv.writer(csv_file, delimiter=',')

url = 'http://sz.58.com/pinpaigongyu/'
response = requests.get(url, verify=False)
html = BeautifulSoup(response.text, "html.parser")
house_list = html.select(".list > li")

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

    print('#'*100)
    print(house_url)
    print(house_name)
    print(location)
    print('#'*100)
    csv_writer.writerow([house_name, location, money, house_url])

csv_file.close()

















