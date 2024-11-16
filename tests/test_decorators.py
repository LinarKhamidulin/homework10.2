import pytest

from src.decorators import my_function, log

#тест декоратора

@pytest.fixture
def my_number_a()-> str:
    number_a = 3
    return number_a


@pytest.fixture
def my_number_b()-> str:
    number_b = 5
    return number_b


def test_my_function(capsys, my_number_a, my_number_b):
    my_function(my_number_a, my_number_b)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n\n"


