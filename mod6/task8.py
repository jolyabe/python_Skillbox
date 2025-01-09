"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""
from typing import List
import re

DIGITS = {2: 'abc',
          3: 'def',
          4: 'ghi',
          5: 'jkl',
          6: 'mno',
          7: 'pqrs',
          8: 'tuv',
          9:'wxyz'}

full_words_list = []

def my_t9(input_number):
    result = []
    if not full_words_list:
        with open('words.txt', 'r') as file:
            [full_words_list.append(line.strip()) for line in file.readlines()]

    letters = map(lambda chars: '[' + DIGITS[int(chars)] + ']', input_number)
    regex_formated = f'(?i)^{"".join(letters)}$'
    result = [word for word in full_words_list if re.match(regex_formated, word)]
    return result

if __name__ == '__main__':
    numbers: str = input()
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
