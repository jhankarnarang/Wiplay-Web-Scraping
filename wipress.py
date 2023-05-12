from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('Wipress.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_Name','Image','Prod_info','Desc'])

source = requests.get('http://www.wipltd.in/wipress.html')
soup = BeautifulSoup(source.content, 'lxml')

# prod_info = soup.select_one('body>div.ab_head>div>div>p')
# prod_name=prod_info.span.text
# print(prod_name)
# prod_img = prod_info.img['src']
# prod_img = f'http://www.wipltd.in/{prod_img}'
# print(prod_img)

# for prod_info1 in soup.select('body>div.ab_head>div>div>p'):
#     prod_desc=prod_info1.text.strip()
#     print(prod_desc)

#csv_writer.writerow([prod_name,prod_img,prod_desc])
    
    

    
#  # prod_name = img.select_one('body>div.ab_head>div>div:nth-child(4)>ul>*')
#     prod_name = img.select_one('ul>*').previous_sibling.strip()
#     print(prod_name)

prod_info = soup.select_one('body>div.ab_head>div>div>p')
prod_name=prod_info.span.text
print(prod_name)
prod_img = prod_info.img['src']
prod_img = f'http://www.wipltd.in/{prod_img}'
print(prod_img)
prod_feature = prod_info.select_one('p>img').next_sibling
print(prod_feature)
prod_spec = prod_info.find_all_next('p')
prod_spec = ' '.join([str(elem) for elem in prod_spec]).replace('<p>','')
prod_spec = prod_spec.replace('<br/>','')
prod_spec = prod_spec.replace('</p>','')
prod_spec = prod_spec.replace('\n\n','')
prod_spec = prod_spec.replace('\n','')
print(prod_spec)
csv_writer.writerow([prod_name,prod_img,prod_feature,prod_spec])



