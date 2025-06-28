import requests
from datetime import datetime
import time

url = f"https://api.nasdaq.com/api/quote/BRK%25sl%25B/historical?assetclass=stocks&fromdate=2024-12-25&limit=9999&todate=2025-06-25&random=1"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url, headers=headers).content
print(content)

with open('data.csv', 'wb') as file:
  file.write(content)