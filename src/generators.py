def filter_by_currency(transactions: list, code: str):
    """функция филтрует по значению "code" """
    try:
        filter_transactions = filter(lambda item: item["operationAmount"]["currency"]["code"] == code, transactions)
        return filter_transactions

    except Exception:
        return


def transaction_descriptions(transactions: list) -> str:
    """функция возвращает описание каждой операции по очереди"""
    try:
        description_ = (transaction.get("description") for transaction in transactions)
        return description_

    except Exception:
        return


def card_number_generator(start: int, end: int):
    """функция сгенерирует номера карт и выдает их в банковском формате"""

    for number in range(start, end + 1):
        card_number_ = str(number)
        while len(card_number_) < 16:
            card_number_ = "0" + card_number_
        card_number_format = f"{card_number_[:4]} {card_number_[4:8]} {card_number_[-8:-4]} {card_number_[-4:]}"

        yield card_number_format
