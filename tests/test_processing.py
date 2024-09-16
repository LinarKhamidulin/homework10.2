import pytest

from src.processing import filter_by_state, sort_by_date

#тесты функции filter_by_state

@pytest.fixture
def test_list_dictionary()-> list:
    list_dictionary = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    return list_dictionary

@pytest.fixture
def my_values()-> str:
    return "EXECUTED"

@pytest.fixture
def my_values_2()-> str:
    return "CANCELED"

@pytest.fixture
def my_values_not()-> str:
    return ""

@pytest.fixture
def my_list_filter()-> list:
    list_filter =[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    return list_filter

@pytest.fixture
def my_list_filter_canceled()-> list:
    list_filter =[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    return list_filter


def test_filter_by_state(test_list_dictionary: list, my_values: list, my_list_filter: list):
    assert filter_by_state(test_list_dictionary, my_values) == my_list_filter


def test_filter_by_state_canceled(test_list_dictionary: list, my_values_2: list,  my_list_filter_canceled: list):
    assert filter_by_state(test_list_dictionary, my_values_2) == my_list_filter_canceled


def test_filter_by_state_not(test_list_dictionary: list, my_values_not: list):
    assert filter_by_state(test_list_dictionary, my_values_not) == []


#тесты функции sort_by_date


@pytest.fixture
def my_sort_by_date_1()-> list:
    sort_by_date_1 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    return sort_by_date_1

@pytest.fixture
def my_sort_by_date_2()-> list:
    sort_by_date_2 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]
    return sort_by_date_2

@pytest.fixture
def my_sort_by_date_3()-> list:
    sort_by_date_2 = [{'id': 615064591, 'state': 'CANCELED', 'date': '10-14-2018T08:21:33.419441'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '09-12-2018-T21:27:25.241689'},
                      {'id': 41428829, 'state': 'EXECUTED', 'date': '07-03-2019T18:35:29.512364'},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '03-07-2019T18:35:29.512364'}]
    return sort_by_date_2


def test_sort_by_date(test_list_dictionary: list, my_sort_by_date_1: list):
    assert sort_by_date(test_list_dictionary) == my_sort_by_date_1


@pytest.fixture
def test_list_dictionary_1()-> list:
    list_dictionary_1 =[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    return list_dictionary_1


def test_sort_by_date_1(test_list_dictionary_1: list, my_sort_by_date_2: list):
    assert sort_by_date(test_list_dictionary_1) == my_sort_by_date_2

@pytest.fixture
def test_list_dictionary_2()-> list:
    list_dictionary_2 =[{'id': 41428829, 'state': 'EXECUTED', 'date': '07-03-2019T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '03-07-2019T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '09-12-2018-T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '10-14-2018T08:21:33.419441'}]
    return list_dictionary_2

def test_sort_by_date_2(test_list_dictionary_2: list, my_sort_by_date_3: list):
    assert sort_by_date(test_list_dictionary_2) == my_sort_by_date_3