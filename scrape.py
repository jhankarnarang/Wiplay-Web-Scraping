from bs4 import BeautifulSoup
import requests
import csv


def scrape(sections, file_names):
    for i in range(len(sections)):
        with open(file_names[i], 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['name', 'img','desc'])

            print(f'> {sections[i]}')
            section_source = requests.get(sections[i])
            soup = BeautifulSoup(section_source.content, 'lxml')
            img = soup.find('div',class_='abt_img')
            prod_img = img.div.img['src']
            print(prod_img)

            desc = soup.find('div',class_='abt_txt')
            prod_name = desc.h4.text
            print(prod_name)
            prod_desc = desc.select('p')
            listToStr = ' '.join([str(elem) for elem in prod_desc])
            s = listToStr.replace('<p>','')
            product_desc = s.replace('</p>','')
            print(product_desc)

            csv_writer.writerow([prod_name,prod_img,product_desc])


            

            
            


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

    sections = [
        'https://finolex.com/wires-cables/',
        'https://finolex.com/switches/',
        'https://finolex.com/led-lightings/',
        'https://finolex.com/fan/',
        'https://finolex.com/finolex-mcb/',
        'https://finolex.com/water-heater/',

           ]

    file_names = [
        './data/wires-cables.csv',
        './data/switches.csv',
        './data/led-lightings.csv',
        './data/fan.csv',
        './data/finolex-mcb.csv',
        './data/water-heater.csv'
    ]

    scrape(sections, file_names)