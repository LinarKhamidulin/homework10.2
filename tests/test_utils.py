import pytest
import json
from dotenv import load_dotenv
from unittest.mock import Mock
from src.utils import exchange_rates_in_rubles, amount_from_the_list

@pytest.fixure
def amount():
    return [{
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    },    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }]


def test_amount_from_the_list(amount: list):
    assert amount_from_the_list(amount) == [48223.05, 79114.93]







@patch('src.utils.exchange_rates_in_rubles')
def test_exchange_rates_in_rubles(mock_get):
    
    mock_get =  ("Транзакции в рублях: 2627938.96, usd в rub: 224541851.5, eur в rub: 0")

    assert exchange_rates_in_rubles() == mock_get

