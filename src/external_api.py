from asyncio import timeout
import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv('API_KEY')
url = os.getenv('URL')

def currency_conversion_rubles_usd(sum_usd):

    headers ={'apikey' : api_key}
    params = {'to': 'RUB',  'from': 'USD', 'amount': sum_usd}

    request = requests.get(url, params=params, headers=headers)

    request.raise_for_status()
    data = request.json()
    return round(data["result"], 2)


def currency_conversion_rubles_eus(eur_sum):
    headers ={'apikey' : api_key}
    params = {'to': 'RUB',  'from': 'EUR', 'amount': eur_sum}

    request = requests.get(url, params=params, headers=headers)

    request.raise_for_status()
    data = request.json()
    return round(data["result"], 2)







