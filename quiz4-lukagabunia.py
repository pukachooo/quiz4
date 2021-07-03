from bs4 import BeautifulSoup
import requests
import random
from time import sleep

file = open('Mouse.csv', 'w', encoding='utf-8_sig')
res = 'სახელი,ფასი\n'
file.write(res)
a = 1
while a < 6:
    url = f"https://adashop.ge/%E1%83%9B%E1%83%90%E1%83%A3%E1%83%A1%E1%83%98/page-{a}"
    r = requests.get(url)
    content = r.text
    b = BeautifulSoup(content, 'html.parser')
    c = b.find('div', {'class': 'grid-list'})
    d = c.find_all('div', {'class': 'ty-column3'})

    for i in d:
        x = i.find('a', {'class': 'product-title'})
        x_name = x['title'].replace(',', '')
        y = i.find('span', {'class': 'ty-price-num'})
        xprice = f"{y.text}"
        file.write(f'{x_name},{xprice}\n')
    a += 1
    sleep(random.randint(15, 20))