from asyncio import timeout
import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv('API_KEY')
url = os.getenv('url')

def currency_conversion_rubles_usd(sum_usd):

    headers ={'apikey' : api_key}
    params = {'to': 'RUB',  'from': 'USD', 'amount': sum_usd}
    to = 'RUB'
    from_ = 'USD'
    amount = sum_usd
    request = requests.get(url, headers=headers)
    #request = requests.get(url,  params=params, headers=headers)
    request.raise_for_status()
    data = request.json()
    return round(data["result"], 2)

def currency_conversion_rubles_eus():
    pass




headers ={'apikey' : "K16LBUCLil1G7oZUvTdXYZFICf8b64V9"}
#params = {'to': 'RUB',  'from': 'USD', 'amount': sum_usd}
to = 'RUB'
from_ = 'USD'
amount = 15
request = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}", headers=headers)
#request = requests.get(url,  params=params, headers=headers)
request.raise_for_status()
data = request.json()
print(round(data["result"], 2))


