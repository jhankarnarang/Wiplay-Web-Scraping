from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.wipltd.in/products.php')
soup = BeautifulSoup(source.content, 'lxml')


for src in soup.find_all('div',class_='col-md4'):
    prod_name = src.div.text
    p_img = src.img['src']
    print(prod_name)
    prod_img = f'http://www.wipltd.in/{p_img}'.replace(' ','%20')
    print(prod_img)