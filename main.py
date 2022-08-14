import requests
from bs4 import BeautifulSoup


def get_info(url):
    '''
    add user agent and get website
    '''
    headers = {'user-agents': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    req = requests.get(url, headers).text
    return req
cafe = input('Введите название компании: ')
print('Подождите...')
cafeSearch = f'https://ufa.flamp.ru/search/{cafe}'
project_urls = []

for i in range(1, 10):
    pages = i
    req = get_info(cafeSearch + f'?page={pages}')
    soup = BeautifulSoup(req, 'lxml')

    articles = soup.find_all('li', class_='list-cards__item list-cards__item--card')
    for article in articles:
        caffe_url = 'https:' + article.find('cat-layouts-card').find('section', class_='card card--basic js-card-link').get('data-url')
        project_urls.append(caffe_url)

req = get_info(cafeSearch)
soup = BeautifulSoup(req, 'lxml')
company_name = soup.find('h3', class_='card__title t-text t-text--bold js-text-fade').get('title')
print(f'По Вашему запросу "{cafe}", найдено {len(project_urls)} компаний "{company_name}"')

# new reviews will be added to the excel file at 12:00 every day by default
# and sent to your telegram chat. Specify the telegram chat (lines 19 and 20),
# specify the update time (line 92) in the parser.py file

