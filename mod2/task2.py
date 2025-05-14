# -------------------------------------
#Задача 2. Средний размер файла
import sys

SIZE_POS = 4

def get_mean_size(ls_output) -> float:
    total, count = 0, 0
    if not ls_output:
        return 'Файлов нет'
    for line in ls_output:
        try:
            total += int(line.split()[SIZE_POS])
        except ValueError:
            return 'Не удается получить размер файла'
        count += 1
    mean_size = total / count
    return mean_size


if __name__ == '__main__':
    lines = sys.stdin.readlines()[1:]
    mean_size = get_mean_size(lines)
    print(mean_size)

# ls -l | python3 task2.py
