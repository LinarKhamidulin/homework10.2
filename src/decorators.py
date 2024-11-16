from functools import wraps
from typing import Union


def log(filename) -> str:
    """функция декаратор автоматически логирует выполнение функции"""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
                if filename:
                    print(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                if filename:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                raise e

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
def my_function(x: Union[str, int], y: Union[str, int]) -> Union[str, int]:
    return x + y


my_function(3, 5)
print(my_function(3, 5))


my_function("3", "5")
print(my_function("3", "5"))

# чисто для теста логирования ошибки

# my_function(3,"5")
# print(my_function(3,"5"))
