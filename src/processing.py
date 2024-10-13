def filter_by_state(list_dictionary: list, state="EXECUTED") -> list:
    '''функция выводит значение по "state", по умолчанию "EXECUTED"'''

    dictionary_new_filter = []
    for dictionary in list_dictionary:
        if dictionary.get("state") == state:
            dictionary_new_filter.append(dictionary)

    return dictionary_new_filter


def sort_by_date(list_dictionary: list, reverse=True) -> list:
    """Функция возвращать новый список, отсортированный по дате"""

    dictionary_new_sort = sorted(list_dictionary, key=lambda x: x["date"], reverse=reverse)

    return dictionary_new_sort
