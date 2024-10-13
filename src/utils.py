import json
import logging
from src.external_api import currency_conversion_rubles_usd, currency_conversion_rubles_eus

logger = logging.getLogger('utils')
file_handler = logging.FileHandler('utils.log')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def amount_from_the_list(file_json) -> list:
    """функция вывода данных из json файла и суммирует их по валюте"""
    amount_sum = []
    rub_sum = 0
    usd_sum = 0
    eur_sum = 0
    try:
        logger.debug(f'Working with a file {file_json}')
        with open(file_json, encoding="utf-8") as f:
            data_file = json.load(f)

        logger.debug(f'working with variables from a file {file_json}')
        for i in data_file:
            if i != {}:
                if i["operationAmount"]["currency"]["code"] == "RUB":
                    rub_sum += float(i["operationAmount"]["amount"])
                if i["operationAmount"]["currency"]["code"] == "USD":
                    usd_sum += float(i["operationAmount"]["amount"])
                if i["operationAmount"]["currency"]["code"] == "EUR":
                    eur_sum += float(i["operationAmount"]["amount"])

        amount_sum.append(round(rub_sum, 2))
        amount_sum.append(round(usd_sum, 2))
        amount_sum.append(round(eur_sum, 2))

        return amount_sum

    except json.JSONDecodeError:
        logger.setLevel(logging.ERROR)
        logger.error("Invalid JSON data.")
        file_error = "Invalid JSON data."

        return file_error
    except KeyError:
        logger.setLevel(logging.ERROR)
        logger.error("Key not found in JSON data.")
        file_error = "Key not found in JSON data."

        return file_error
    except TypeError:
        logger.setLevel(logging.ERROR)
        logger.error("Object of type set is not JSON serializable.")
        file_error = "Object of type set is not JSON serializable."

        return file_error


def exchange_rates_in_rubles(amount_sum: list) -> str:
    """Функция конвертации значениий из иностроной валюты в рубли"""

    logger.info(f'working with variables from functions "amount_from_the_list" ')
    if amount_sum[1] >= 0:
        usd = amount_sum[1]
        usd_sum_in_rub = currency_conversion_rubles_usd(usd)
    if amount_sum[2] > 0:
        eur = amount_sum[2]
        eur_sum_in_rub = currency_conversion_rubles_eus(eur)
    elif amount_sum[2] == 0:
        eur_sum_in_rub = 0

    result = f"Транзакции в рублях: {amount_sum[0]}, usd в rub: {round(usd_sum_in_rub, 2)}, eur в rub: {round(eur_sum_in_rub, 2)}"

    return result


amount_sum = amount_from_the_list("../data/operations.json")
print(exchange_rates_in_rubles(amount_sum))
