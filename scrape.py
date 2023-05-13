from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://www.wipltd.in/plywood.php')
soup = BeautifulSoup(source.content, 'lxml')



for img in soup.find_all('div',class_='col-md12'):
    p_img = img.div.img['src'].replace(' ','%20')
    prod_img = f'http://www.wipltd.in/{p_img}'
    print(prod_img)

    prod_applications = img.find('li').text
    print(prod_applications)
    prod_feature = img.find_all('li')[1:]
    p_features = u' '.join(str(e) for e in prod_feature).replace('<li>','') 
    prod_features = p_features.replace('</li>','')
    print(prod_features)

    # prod_name = img.select_one('body>div.ab_head>div>div:nth-child(4)>ul>*')
    prod_name = img.select_one('ul>*').previous_sibling.strip()
    print(prod_name)

        

    

