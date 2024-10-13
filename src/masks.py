import logging

logger = logging.getLogger('mask')
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def get_mask_card_number(card_number: str) -> str:
    """функция создает маску карты, выводя номер карты разделя их пробелом, 6 символ меняются на *"""

    logger.info('performing a card number mask')
    logger.error("card number mask execution error")
    mask_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """функция создает маску карты показывая ** последние 4 символа"""

    logger.info('The operation of the account mask')
    logger.error("account number mask execution error")
    mask_card_number = f"**{account_number[-4:]}"

    return mask_card_number


