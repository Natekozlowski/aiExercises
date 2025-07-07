import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

APIKEY = os.getenv("WEATHER_API_KEY")


def get_weather(city, units='metric', api_key={APIKEY}):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
  r = requests.get(url)
  content = r.json()
  with open('data.txt', 'a') as file:
    for dicty in content['list']:
      file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")

print(get_weather(city='Annapolis'))