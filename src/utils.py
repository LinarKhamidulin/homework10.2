import os
import json
from logging import exception

from src.external_api import currency_conversion_rubles_usd, currency_conversion_rubles_eus


def filter(file_json):
    rub_sum = 0
    usd_sum = 0
    eur_sum = 0
    try:
        with open(file_json, encoding='utf-8') as f:
            data_file = json.load(f)

        for i in data_file:
            if i != {}:
                if i["operationAmount"]["currency"]["code"] == "RUB":
                    rub_sum += float(i["operationAmount"]["amount"])
                if i["operationAmount"]["currency"]["code"] == "USD":
                    usd_sum += float(i["operationAmount"]["amount"])
                    usd_sum_in_rub = currency_conversion_rubles_usd(usd_sum)
                if i["operationAmount"]["currency"]["code"] == "EUR":
                    eur_sum += float(i["operationAmount"]["amount"])
                    #eur_sum_in_rub = currency_conversion_rubles_eus(eur_sum)

        return round(rub_sum, 2), round(usd_sum_in_rub, 2), round(eur_sum, 2)
    except json.JSONDecodeError:
        file_ = "Invalid JSON data."
        return file_
    except KeyError:
        file_ = "Key not found in JSON data."
        return file_
    except TypeError:
        file_ = "Object of type set is not JSON serializable."
        return file_


'''
def main(file_json):
    data_ = filter(file_json)
    print(data_)
'''

#if __name__ == '__utils__':
print(filter('../data/operations.json'))
    #main('/data/operations.json')



