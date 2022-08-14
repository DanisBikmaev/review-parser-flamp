import pandas as pd
from bs4 import BeautifulSoup
import datetime as dt
import main
from datetime import timedelta
import requests
import schedule
import time


def all_func():
    '''
    all function: parsing, data saving in excel file, sending telegramm massage
    '''
    def telegram_bot_sendtext(message):
        '''
        sending new feedbacks for telegram channel with bot
        '''
        bot_token = '   ' # token tgBot
        chat_id = '     ' # id tgChat
        send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
        response = requests.get(send_text)
        return response.json()

    def get_datalist(site):
        '''
        getting html code from website and getting elements for data parsing
        '''
        result = requests.get(site)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')

        sourceReviews = soup.find_all('cat-brand-ugc-date') # getting review source element 
        userNames = soup.find_all('a', class_='link name t-text t-text--bold') # getting review author element
        datatimes = soup.find_all('cat-brand-ugc-date') # getting date and time review
        ratings = soup.find_all('li', class_='review-estimation__item list__item t-text t-text--micro t-text--bold review-estimation__item--checked') # getting review rating
        textReviews = soup.find_all('div',
         class_='t-text t-rich-text ugc-item__text ugc-item__text--full js-ugc-item-text-full') # getting review text
        return sourceReviews, userNames, datatimes, ratings, textReviews

    def get_source(value):
        '''
        get source review
        '''
        sourceReview = value.get('url')
        return 'https:' + sourceReview

    def get_data(value):
        '''
        get review author, raiting, text
        '''
        result = value.text.strip()
        return result

    def get_time(value):
        '''
        get date and time review
        '''
        dt = value.get('date')[:-6]
        return dt

    point = dt.datetime.combine(dt.date.today() - timedelta(days=1), dt.time(12)) # last checking for new reviews
    for j in all_website:
        sourceReviews, userNames, datatimes, ratings, textReviews = get_datalist(j)
        for i in range(len(sourceReviews)):
            sms = ''
            t = dt.datetime.strptime(get_time(datatimes[i]), '%Y-%m-%dT%H:%M:%S') #format date
            if t >= point:
                sourceReview = get_source(sourceReviews[i])
                usname = get_data(userNames[i])
                rating = get_data(ratings[i])
                text = get_data(textReviews[i])
                line = [sourceReview, usname, t, rating, text]
                df.loc[len(df.index)] = line
                print('-' * 50)
                if int(df.duplicated().any()) == 1: #checking for data duplicates
                    df.drop_duplicates() # delete data duplicates
                else:
                    for j in range(len(fieldnames)):
                        sms += f'{fieldnames[j]} : {line[j]} \n'
                    print(sms)
                    telegram_bot_sendtext(sms) # tg massage about new review
                    df.to_excel('test_res.xlsx') # add new review in excel file
    return df


if __name__ == '__main__':
    df = pd.DataFrame(columns=['sourceReview', 'name', 'time', 'rating', 'text'])
    all_website = main.project_urls
    fieldnames = ['Источник', 'Автор', 'Время', 'Рейтинг', 'Отзыв']
    #schedule.every(1).minutes.do(all_func) #for test: check updates every 1 minute
    schedule.every().day.at("12:00").do(all_func) # check updates every day at 12:00
    while True:
        print(dt.datetime.now()) #timeout sending telegramm sms
        schedule.run_pending()
        time.sleep(10)
