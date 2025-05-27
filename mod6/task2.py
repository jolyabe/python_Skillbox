# -------------------------------------
# Задача 2. Сложность пароля
import getpass
import hashlib
import logging
import re
import sys

logger = logging.getLogger(__name__)
words = []

def initialize_words():
    with open('words.txt', encoding='utf-8') as file:
        global words
        words = file.readlines() # формируем список слов из файла
        words = map(lambda word: word.lower().strip(), words) # приводим к нижнему регистру и убираем символы новой строки
        words = sorted(words) # сортируем список слов


def binary_search(password_piece: str) -> str:
    '''
    Ищет фрагмент пароля в списке англ. слов.
    '''
    left, right = 0, len(words) - 1
    logger.debug(f"Старт бинарного поиска")
    
    while left <= right:
        
        mid = (left + right) // 2
        if password_piece == words[mid]:
            return True
        elif password_piece < words[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return False


def is_strong_password(password: str) -> bool:
    '''checking password, if piece of password was found in file - return True,
    else - return None'''
    logger.debug("Проверка пароля на сложность")
    password = password.lower()
    if not words:
        initialize_words()

    words_in_password = re.findall(r'[a-z]{5,}', password)
    for word in words_in_password:
        logger.debug(f"Поиск {word} в файле слов")
        res_of_search = binary_search(word)
        if res_of_search:
            logger.debug(f"{word} - слово из словаря")
            return False
    logger.debug("Сложный пароль!")
    return True


def input_and_check_password() -> bool:
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    if not is_strong_password(password):
        logger.warning("Введен слабый пароль")
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == '890a700a1d465e183581dcf4d1eb25d9':
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

# p45sw0rd
