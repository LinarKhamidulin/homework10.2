import pytest

from src.widget import get_date, mask_account_card

# тесты функции mask_account_card

@pytest.mark.parametrize("str_data, expected",[("Visa Platinum 7000792289606361","Visa Platinum 7000 79** **** 6361",),
                                    ("Visa Platinum 70007922896", ""),
                                    ("Счет 73654108430135874305", "Счет **4305"),
                                    ("Счет 7365410843013587", "Счет 7365 41** **** 3587")])


def test_1_mask_account_card(str_data: str, expected: str):
    assert mask_account_card(str_data) == expected


# тесты функции get_date

@pytest.fixture
def my_data()-> str:
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def my_data_alternative()-> str:
    return "03-11-2024"

def test_get_date(my_data: str):
    assert get_date(my_data) == "11.03.2024"


def test_get_date_alternative(my_data_alternative: str):
    assert get_date(my_data_alternative) == "24.-2.03-1"

def test_get_date_not():
    assert get_date("") == ".."
