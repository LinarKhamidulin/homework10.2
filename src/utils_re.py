import re
from collections import Counter


def filter_parameters_from_the_user(parameters: dict)-> dict:
    '''функция для проверки ввода параметров для фильтрования'''
    try:
        file_to_process_ = re.findall(r"1|2|3", parameters.get("process"), flags=re.IGNORECASE)
        filter_by_status_ = re.findall(r"EXECUTED|CANCELED|PENDING", parameters.get("status"), flags=re.IGNORECASE)
        filter_by_data_ = re.findall(r"да|нет", parameters.get("data"), flags=re.IGNORECASE)
        sort_in_ascending_or_descending_order_ = re.findall(
            r"по возрастанию|по убыванию", parameters.get("ascending_or_descending"), flags=re.IGNORECASE
        )
        filter_by_currency_ = re.findall(r"да|нет", parameters.get("currency"), flags=re.IGNORECASE)
        filter_by_word_ = re.findall(r"да|нет", parameters.get("words"), flags=re.IGNORECASE)

        parameters_from_the_user = {
            "process": file_to_process_[0],
            "status": filter_by_status_[0],
            "data": filter_by_data_[0],
            "ascending_or_descending": sort_in_ascending_or_descending_order_[0],
            "currency": filter_by_currency_[0],
            "words": filter_by_word_[0]
        }

        return parameters_from_the_user

    except Exception:
        return f"Указаны не верные параметры для сортировки {parameters}"


def counting_operations(list_data: list)-> dict:
    '''функция для фильтрования и подсчета операции'''
    list_ = []
    for dist in list_data:
        description = re.findall("\D+", dist['description'], flags=0)
        list_.append(*description)
        counted = Counter(list_)

    return counted