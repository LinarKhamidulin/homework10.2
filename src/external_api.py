import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv('API_KEY')
url = os.getenv('URL')

def currency_conversion_rubles_usd(sum_usd: int)-> int:
    '''функция обращения к api по url для конвертации валеты из USD в RUB'''

    headers ={'apikey' : api_key}
    params = {'to': 'RUB',  'from': 'USD', 'amount': sum_usd}

    request = requests.get(url, params=params, headers=headers)

    request.raise_for_status()
    data = request.json()
    return data['result']


def currency_conversion_rubles_eus(eur_sum: int)-> int:
    '''функция обращения к api по url для конвертации валеты из EUR в RUB'''

    headers ={'apikey' : api_key}
    params = {'to': 'RUB',  'from': 'EUR', 'amount': eur_sum}

    request = requests.get(url, params=params, headers=headers)

    request.raise_for_status()
    data = request.json()
    return data['result']







