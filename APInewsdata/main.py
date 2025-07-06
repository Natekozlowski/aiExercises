import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

URL = os.getenv("API_URL")
APIKEY = os.getenv("API_KEY")


def getNews(topic, from_date, to_date, api, language='en'):
    URL =  f'https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api}'
    r = requests.get(URL)
    content = r.json()
    articles = content['articles']
    with open('data.txt', 'wt') as file:
        for article in articles:
            file.write(f"TITLE\n{article['title']}\nDESCRIPTION\n{article['description']}\n")

getNews(topic='nvidia', from_date='2025-07-01', to_date='2025-07-05', api=APIKEY)