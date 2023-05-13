from bs4 import BeautifulSoup
import requests
import csv


csv_file = open('HardBoards.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Prod_Name','Prod_info'])


source = requests.get('http://www.wipltd.in/hardboards.php')
soup = BeautifulSoup(source.content, 'lxml')

main = soup.find('div',class_='ab_head')
prod_name = main.h3.text
print(prod_name)
prod_info = main.p.text.strip()
print(prod_info)

csv_writer.writerow([prod_name,prod_info])


