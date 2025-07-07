import requests
import json

url = 'https://api.languagetool.org/v2/check'
# Dictionary
data = {
    'text': 'Ths is a nive fay',
    'language' : 'auto'
}
# a string is made of characters and the dictionary is recognized by Python as a more compound data type
response = requests.post(url, data=data)
result = json.loads(response.text)
print(result)