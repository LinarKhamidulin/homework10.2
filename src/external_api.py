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
    params = {'amount': sum_usd, 'from': 'USD', 'to': 'RUB'}

    request = requests.get(url,  params=params, headers=headers)
    request.raise_for_status()
    data = request.json()
    return round(data["result"], 2)

def currency_conversion_rubles_eus():
    pass
