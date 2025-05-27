# -------------------------------------
# Задача 1. Аутентификация
import getpass
import hashlib
import logging
import sys

logger = logging.getLogger(__name__)

def input_and_check_password() -> bool:
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == '5f4dcc3b5aa765d61d8327deb882cf99':
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


if __name__ == '__main__':
    logging.basicConfig(
        filename='stderr.txt',
        filemode='w',
        encoding='utf-8',
        level=logging.INFO,
        datefmt="%H:%M:%S",
        format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попытки")

    while count_number > 0:
        if input_and_check_password():
            sys.exit(0)
        count_number -= 1

    logger.error("Пользователь трижды ввёл не правильный пароль!")
    sys.exit(1)

# password
