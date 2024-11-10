import pytest
import json
from dotenv import load_dotenv
from unittest.mock import Mock, mock_open
from unittest.mock import patch

from src.external_api import currency_conversion_rubles_eus
from src.utils import exchange_rates_in_rubles, amount_from_the_list

@pytest.fixture
def my_list_filter()-> list:
    list_filter = [
    {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {
            "name": "руб.",
            "code": "RUB"
         }
        }
    },
    {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
          }
       }
    }
    ]
    return list_filter


@patch("builtins.open", new_callable=mock_open, read_data="my_list_filter")
def test_exchange_rates_in_rubles(mock_file):
    assert open("path/to/open").read() == "my_list_filter"
    mock_file.assert_called_with("path/to/open")




