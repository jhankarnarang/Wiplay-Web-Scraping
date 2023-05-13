from bs4 import BeautifulSoup
import requests
import csv

t=[]
def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Prod_name','Prod_image','Prod_applications','Prod_feature'])

            print(f'> {sections[i]}')
            source = requests.get(sections[i])
            soup = BeautifulSoup(source.content, 'lxml')
            try:
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
                    prod_name = img.select_one('ul>*').previous_sibling.strip()
                    print(prod_name)
                    csv_writer.writerow([prod_name,prod_img,prod_applications,prod_features])
            except:
                print('')
            
            try:
                for src in soup.find_all('div',class_='col-md4'):
                    prod_name = src.div.text
                    p_img = src.img['src']
                    print(prod_name)
                    prod_img = f'http://www.wipltd.in/{p_img}'.replace(' ','%20')
                    print(prod_img)
                    csv_writer.writerow([prod_name,prod_img])
            except:
                print('')

            

            



            
            


if __name__ == '__main__':

    '''
    usage:
    -> install requirements
    -> verify:
        - all site sections are listed in `sections`
        - all sites have a corresponding csv file `file_names`
        - all paths to the csv file are correct
    -> run
    '''

    sections = ['http://www.wipltd.in/plywood.php',
                'http://www.wipltd.in/hardboards.php',
                'http://www.wipltd.in/densified_wood.php',
                'http://www.wipltd.in/products.php',
                'http://www.wipltd.in/woode_floor.php']  

    file_names = ['./data/plywood.csv',
                './data/hardboard.csv',
                './data/densified_wood.csv',
                './data/furniture.csv',
                './data/wooden_flooring.csv']

    scrape(sections, file_names)