from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_data_numbers: str) -> str:
    """функция отделяет наименования карты от номера, выводя наименования маску номера карты"""

    card_number = "".join(number if number.isdigit() else "" for number in card_data_numbers)
    name_card = "".join("" if values_.isdigit() else values_ for values_ in card_data_numbers)

    if len(card_number) == 16:
        card_number_mask = get_mask_card_number(card_number)
        mask_card_number_name = name_card + card_number_mask
    elif len(card_number) == 20:
        mack_account_number = get_mask_account(card_number)
        mask_card_number_name = name_card + mack_account_number
    else:
        mask_card_number_name = ""

    return mask_card_number_name


def get_date(date_line: str) -> str:
    """функция обработки даты в формат ДД.ММ.ГГГГ"""
    return f"{date_line[8:10]}.{date_line[5:7]}.{date_line[0:4]}"
