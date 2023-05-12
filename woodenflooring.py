from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.wipltd.in/woode_floor.php')
soup = BeautifulSoup(source.content, 'lxml')

for img in soup.find_all('div',class_='col-md12'):
    p_img = img.div.img['src']
    prod_img = f'http://www.wipltd.in/{p_img}'
    print(prod_img)
    prod_applications = img.find('li').text
    print(prod_applications)
    for prod_feature in img.find_all('li')[1:]:
        prod_features = prod_feature.text
        print(prod_features)

    


