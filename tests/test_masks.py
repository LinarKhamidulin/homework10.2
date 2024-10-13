import pytest

from src.masks import get_mask_card_number, get_mask_account


#Тест функции get_mask_card_number

@pytest.fixture
def my_str_card_number()-> str:
    return "7000792289606361"

@pytest.fixture
def my_str_card_number_1()-> str:
    return "700079228960"

def test_get_mask_card_number(my_str_card_number: str):
    assert get_mask_card_number(my_str_card_number) == "7000 79** **** 6361"


def test_get_mask_card_number_short(my_str_card_number_1: str):
    assert get_mask_card_number(my_str_card_number_1) == "7000 79** **** 8960"


def test_get_mask_card_number_not_data():
    assert get_mask_card_number("") == " ** **** "


#Тест функции get_mask_account

@pytest.fixture
def my_str_account()-> str:
    return "73654108430135874305"

@pytest.fixture
def my_str_account_2()-> str:
    return "7365410843013587"

def test_get_mask_account(my_str_account: str):
    assert get_mask_account(my_str_account) == "**4305"


def test_get_mask_account_short(my_str_account_2: str):
    assert get_mask_account(my_str_account_2) == "**3587"


def test_get_mask_account_not_data():
    assert get_mask_account(" ") == "** "
