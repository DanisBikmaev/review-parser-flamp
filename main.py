import requests
from bs4 import BeautifulSoup


def get_info(url):
    '''
    add user agent and get website
    '''
    headers = {'user-agents': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    req = requests.get(url, headers).text
    return req

cafeSearch = 'https://ufa.flamp.ru/search/vkusno_i_tochka'
project_urls = []

for i in range(1, 3):
    pages = i
    req = get_info(cafeSearch + f'?page={pages}')
    soup = BeautifulSoup(req, 'lxml')

    articles = soup.find_all('li', class_='list-cards__item list-cards__item--card')
    for article in articles:
        caffe_url = 'https:' + article.find('cat-layouts-card').find('section', class_='card card--basic js-card-link').get('data-url')
        project_urls.append(caffe_url)
