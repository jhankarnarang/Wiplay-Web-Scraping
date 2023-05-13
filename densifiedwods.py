from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.wipltd.in/densified_wood.php')
soup = BeautifulSoup(source.content, 'lxml')

for img in soup.find_all('div',class_='col-md12'):
    prod_img = img.div.img['src']
    print(prod_img)
    prod_applications = img.find('li').text
    print(prod_applications)
    for prod_feature in img.find_all('li')[1:]:
        prod_features = prod_feature.text
        print(prod_features)

    prod_name = img.ul
    print(prod_name)


