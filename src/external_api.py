import logging
import os
from dotenv import load_dotenv
import requests

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("utils.log")
file_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
logger.setLevel(logging.ERROR)



load_dotenv()
api_key = os.getenv('API_KEY')
url = os.getenv('URL')

def currency_conversion_rubles_usd(sum_usd: int)-> int:
    '''функция обращения к api по url для конвертации валеты из USD в RUB'''
    try:
        headers ={'apikey' : api_key}
        params = {'to': 'RUB',  'from': 'USD', 'amount': sum_usd}

        request = requests.get(url, params=params, headers=headers)

        #request.raise_for_status()
        data = request.json()
        return data['result']

    except KeyError:

        logger.error("Key not found in JSON data.")
        file_error = "Key not found in JSON data."

        return file_error


def currency_conversion_rubles_eus(eur_sum: int)-> int:
    '''функция обращения к api по url для конвертации валеты из EUR в RUB'''

    try:
        headers ={'apikey' : api_key}
        params = {'to': 'RUB',  'from': 'EUR', 'amount': eur_sum}

        request = requests.get(url, params=params, headers=headers)

        #request.raise_for_status()
        data = request.json()
        return data['result']

    except KeyError:

        logger.error("Key not found in JSON data.")
        file_error = "Key not found in JSON data."

        return file_error


#print(currency_conversion_rubles_usd(1))



