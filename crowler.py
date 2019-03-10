import csv
from datetime import datetime
from bs4 import BeautifulSoup
import requests

def get_html(url):
    r = requests.get(url)
    return r.text

def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all('ul',class_='pagn')
    # print(data)

    links = []

        # a = href.find('a', attrs={'data-page': %s).get('href')
    # for i in range(1, 251):
    #     link = '/kyrgyzstan/mobilnye-telefony-i-aksessuary?page=%s' % i
    #     base_url = 'https://lalafo.kg' + link
        # print(base_url)
        # links.append(link)
        # for i in range(int(a),249):
            # i.get('href')
        # link = 'https://lalafo.kg' + a
            # links.append(i)

        # return links

    print(links)

def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        name = soup.find_all('a', class_='name')

        # print(name)
    except:
        name = ''
    try:
        price = soup.find_all('div', class_='price')
    except:
        price = ''

    data = {'name': name,
            'price': price,}
    for key,value in data.items():
        for x in value:
            print(x.get_text())
            with open('lalafo.csv', 'a') as f:
                writer = csv.writer(f)

                writer.writerow( (data['name'],
                                 data['price']), )

    # print(data)
        # print(data)
                # write_csv(data)

    return data


# def write_csv(data):

        # print(data['name'],data['price'] 'parsed')

def main():
    # for i in range(1, 250):
    #     link = '/kyrgyzstan/mobilnye-telefony-i-aksessuary?page=%s' % i
    #     base_url = 'https://lalafo.kg' + link
    base_url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/'
    while base_url:
        print(base_url)
        r = requests.get(base_url)
        soup = BeautifulSoup(r.text,'html.parser')
        li = soup.find_all('li',{'class': 'pagn-next'})
        for url in li:
            res = url.find('a').get('href')
            print(res)
            # print(base_url)
            if res:
                result = 'https://lalafo.kg' + res
            else:
                break

        all_links_data = get_page_data(get_html(base_url))
        # write_csv(all_links_data)
    # start = datetime.now()
    # url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary/'
    # all_links = get_all_links(get_html(url))
    # print(all_links)
    # all_data = get_page_data(get_html(url))

    # print(all_links)

main()

