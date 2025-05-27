# -------------------------------------
# Задача 8. Т9
import re
from typing import List

DIGITS = {2: 'abc',
          3: 'def',
          4: 'ghi',
          5: 'jkl',
          6: 'mno',
          7: 'pqrs',
          8: 'tuv',
          9: 'wxyz'}

full_words_list = []

def my_t9(input_number):

    if not full_words_list:
        with open('words.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                full_words_list.append(line.rstrip())

    letters = map(lambda chars: '[' + DIGITS[int(chars)] + ']', input_number)
    regex_formated = f'(?i)^{"".join(letters)}$'
    result = [word for word in full_words_list if re.match(regex_formated, word)]
    return result

if __name__ == '__main__':
    numbers: str = input()
    words: List[str] = my_t9(numbers)
    print(*words)
