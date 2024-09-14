def get_mask_card_number(card_number: str) -> str:
    """функция создает маску карты, выводя номер карты разделя их пробелом, 6 символ меняются на *"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """функция создает маску карты показывая ** последние 4 символа"""

    mask_card_number = f"**{account_number[-4:]}"

    return mask_card_number
