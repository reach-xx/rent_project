from bs4 import BeautifulSoup
import requests
import re


url = 'http://sz.58.com/pinpaigongyu/'
response = requests.get(url, verify=False)
html = BeautifulSoup(response.text, "html.parser")
house_list = html.select(".list > li")

for house in house_list:
    value = house.select('div')
    house_money = house.select(".money")[0].select("b")[0].string.encode("utf8")
    house_name = house.select('.des')[0].select('h2')[0]
    print('#'*100)
    print(house_name)
    print(house_money)
    # print(value[0], value[2])
    print('#'*100)



















