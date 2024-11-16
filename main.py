from src.utils_re import filter_parameters_from_the_user, counting_operations
from src.widget import get_date, mask_account_card
from src.utils import open_file_json
from src.handler_CSV_Excel import reading_a_file_csv, read_excel_file


def main() -> dict:
    '''Главная функция принимает данные от пользователя для дальнейшей обработки'''
    print(
        """lower()
    Программа: Привет! Добро пожаловать в программу работы
    с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
    )
    name_user = input("Имя ")

    file_to_process = input(f"{name_user}, выберите файл для обработки ")
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    filter_by_status = input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
    filter_by_data = input("Отсортировать операции по дате? Да/Нет ")
    sort_in_ascending_or_descending_order = input("Отсортировать по возрастанию или по убыванию? ")
    filter_by_currency_ = input("Выводить только рублевые транзакции? Да/Нет ")
    filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    print(f"Распечатываю итоговый список транзакций для {name_user}")

    parameters_from_the_user = {
        "process": file_to_process,
        "status": filter_by_status,
        "data": filter_by_data,
        "ascending_or_descending": sort_in_ascending_or_descending_order,
        "currency": filter_by_currency_,
        "words": filter_by_word
    }
    return parameters_from_the_user


def parameter_handler(parameters: dict)-> str:
    '''Функция обработки данных из файлов JSON, CSV, XLSX'''
    try:

        if parameters["process"] == "1":
            #обработки данных из файлов JSON

            file_open = open_file_json(parameters)
            #выбор подсчета
            #по операциям
            if parameters["words"] == "да":
                counted = counting_operations(file_open)
            #все операции
            elif parameters["words"] == "нет":
                counted = 0
                for i in file_open:
                    if i != {}:
                        counted += 1

            print(f"Всего банковских операций в выборке: {counted}")

            for i in file_open:
                date_of_the_operation = get_date(i["date"])
                operation = i["description"]
                if "from" in i.keys():
                    recipient_ = mask_account_card(i["to"])
                    sender = mask_account_card(i["from"])
                else:
                    recipient_ = mask_account_card(i["to"])

                amount = i["operationAmount"]["amount"]
                name_currency = i["operationAmount"]["currency"]["name"]

                print(f"{date_of_the_operation}: {operation}.")
                if sender != "":
                    print(f"{recipient_} -> {sender}.")
                else:
                    print(recipient_)
                print(f"сумма: {amount} {name_currency}\n")

        elif parameters["process"] == "2":
            #обработки данных из файлов CSV
            file_open = reading_a_file_csv(parameters)
            #выбор подсчета
            #по операциям
            if parameters["words"] == "да":
                counted = counting_operations(file_open)
            #все операции
            elif parameters["words"] == "нет":
                counted = 0
                for i in file_open:
                    if i != {}:
                        counted += 1

            print(f"Всего банковских операций в выборке: {counted}")
            for i in file_open:
                date_of_the_operation = get_date(i["date"])
                operation = i["description"]
                if "from" in i.keys():
                    recipient_ = mask_account_card(i["to"])
                    sender = mask_account_card(i["from"])
                else:
                    recipient_ = mask_account_card(i["to"])
                amount = i["amount"]
                name_currency = i["currency_name"]

                print(f"{date_of_the_operation}: {operation}.")
                if sender != "":
                    print(f"{recipient_} -> {sender}.")
                else:
                    print(recipient_)
                print(f"сумма: {amount} {name_currency}\n")

        elif parameters["process"] == "3":
            #обработки данных из файлов XLSX
            file_open = read_excel_file(parameters)
            #выбор подсчета
            #по операциям
            if parameters["words"] == "да":
                counted = counting_operations(file_open)
            #все операции
            elif parameters["words"] == "нет":
                counted = 0
                for i in file_open:
                    if i != {}:
                        counted += 1

            print(f"Всего банковских операций в выборке: {counted}")
            for i in file_open:
                date_of_the_operation = get_date(i["date"])
                operation = i["description"]
                print(f"{date_of_the_operation}: {operation}.")

                if i["description"] != "Открытие вклада":
                    recipient_ = mask_account_card(i["to"])
                    sender = mask_account_card(i["from"])
                    print(f"{recipient_} -> {sender}.")
                else:
                    recipient_ = mask_account_card(i["to"])
                    print(recipient_)
                amount = i["amount"]
                name_currency = i["currency_name"]
                print(f"сумма: {amount} {name_currency}\n")

    except TypeError:
        return f"ошибка TypeError"

    except Exception:
        return f"Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"


request_parameters = main()
print(filter_parameters_from_the_user(request_parameters))
parameters_from_the_user = filter_parameters_from_the_user(request_parameters)
user_parameters = parameter_handler(parameters_from_the_user)
print(user_parameters)
