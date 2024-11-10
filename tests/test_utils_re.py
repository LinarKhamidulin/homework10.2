import pytest

from src.utils_re import filter_parameters_from_the_user


#обычноый ввод данных
@pytest.fixture
def test_parameters()-> list:
    parameters = {
        "process": "1",
        "status": "EXECUTED",
        "data": "да",
        "ascending_or_descending": "по возрастанию",
        "currency": "да",
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
    }
    return f"Указаны не верные параметры для сортировки {parameters}"

def test_filter_parameters_from_the_user_error(test_parameters_error: dict, parameters_error: dict):
    assert filter_parameters_from_the_user(test_parameters_error) == parameters_error
