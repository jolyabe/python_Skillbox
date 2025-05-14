# -------------------------------------
# Задача 3. Дешифратор
import sys

def decrypt(encryption: str) -> str:
    stack = []
    for c in encryption:
        stack.append(c)
        if len(stack) > 2 and stack[-2:] == ['.', '.']:
            del stack[-1] # удаляем последнюю точку
            del stack[-1] # удаляем предпоследнюю точку
            del stack[-1] # удаляем символ
    return ''.join(filter(lambda x: x != '.', stack))


if __name__ == '__main__':
    data: str = sys.stdin.read()
    print(decrypt(data))

# echo "абраа..-кадабра" | python3 decrypt.py
