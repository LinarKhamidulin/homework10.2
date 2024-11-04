from unittest.mock import patch

from src.external_api import currency_conversion_rubles_eus, currency_conversion_rubles_usd


@patch("requests.get")
def test_api_eus(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'result': 100}
    assert currency_conversion_rubles_eus(10) == 100


@patch("requests.get")
def test_api_usd(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'result': 100}
    assert currency_conversion_rubles_usd(10) == 100

