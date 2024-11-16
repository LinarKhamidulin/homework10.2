import pytest

from src.utils_re import filter_parameters_from_the_user, counting_operations

# тесты для filter_parameters_from_the_user

#обычноый ввод данных
@pytest.fixture
def test_parameters()-> list:
    parameters = {
        "process": "1",
        "status": "EXECUTED",
        "data": "да",
        "ascending_or_descending": "по возрастанию",
        "currency": "да",
        "words": "да"
    }
    return parameters

@pytest.fixture
def parameters_()-> list:
    parameters = {
        "process": "1",
        "status": "EXECUTED",
        "data": "да",
        "ascending_or_descending": "по возрастанию",
        "currency": "да",
        "words": "да"
    }
    return parameters

def test_filter_parameters_from_the_user(test_parameters: dict, parameters_: dict):
    assert filter_parameters_from_the_user(test_parameters) == parameters_

# Тест на ошибку пользователь не вводит данные
@pytest.fixture
def test_parameters_not()-> list:
    parameters = {
        "process": "",
        "status": "",
        "data": "",
        "ascending_or_descending": "",
        "currency": "",
        "words": ""
    }
    return parameters

@pytest.fixture
def parameters_not()-> list:
    parameters = {
        "process": "",
        "status": "",
        "data": "",
        "ascending_or_descending": "",
        "currency": "",
        "words": ""
    }
    return f"Указаны не верные параметры для сортировки {parameters}"

def test_filter_parameters_from_the_user_not(test_parameters_not: dict, parameters_not: dict):
    assert filter_parameters_from_the_user(test_parameters_not) == parameters_not

#ввод данных с ошибкой
@pytest.fixture
def test_parameters_error()-> list:
    parameters = {
        "process": "6",
        "status": "EXECUTE",
        "data": "д",
        "ascending_or_descending": "по возию",
        "currency": "да",
        "words": "да"
    }
    return parameters

@pytest.fixture
def parameters_error()-> list:
    parameters = {
        "process": "6",
        "status": "EXECUTE",
        "data": "д",
        "ascending_or_descending": "по возию",
        "currency": "да",
        "words": "да"
    }
    return f"Указаны не верные параметры для сортировки {parameters}"

def test_filter_parameters_from_the_user_error(test_parameters_error: dict, parameters_error: dict):
    assert filter_parameters_from_the_user(test_parameters_error) == parameters_error


# тесты для counting_operations

@pytest.fixture
def parameters_counting()-> list:
    parameters = [
        {
        'id': '4653425',
        'state': 'EXECUTED',
        'date': '2020-03-10T07:48:21Z',
        'amount': '22131',
        'currency_name': 'Ruble',
        'currency_code': 'RUB',
        'from': '',
        'to': 'Счет 58936710508356884628',
        'description': 'Открытие вклада'
        },
        {
        'id': '2195935',
        'state': 'EXECUTED',
        'date': '2020-05-10T08:19:35Z',
        'amount': '29722',
        'currency_name': 'Ruble',
        'currency_code': 'RUB',
        'from': 'Visa 7657178713716531',
        'to': 'Mastercard 5442625865778510',
        'description': 'Перевод с карты на карту'
        },
        {
        'id': '2300619',
        'state': 'EXECUTED',
        'date': '2020-06-12T18:50:27Z',
        'amount': '32753',
        'currency_name': 'Ruble',
        'currency_code': 'RUB',
        'from': 'Discover 8926691998863176',
        'to': 'Discover 9331952063031046',
        'description': 'Перевод с карты на карту'
        }
    ]

    return parameters
'''

@pytest.fixture
def return_counting()-> list:
    return_ = Counte({'Перевод с карты на карту': 2, 'Открытие вклада': 1})
    return return_

def test_counting_operations(parameters_counting: list, return_counting):
    assert counting_operations(parameters_counting) == return_counting
'''