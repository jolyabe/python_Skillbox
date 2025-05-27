# -------------------------------------
# Задача 4. Анализируем логи
import json
import subprocess
import shlex
from itertools import groupby

LOG_FILENAME = 'skillbox_json_messages.log'

def get_messages_number_by_type(log_data):
    '''Сколько было сообщений каждого уровня за сутки'''

    msg_type_per_day = {}

    for log_line in log_data:
        msg_type_per_day[log_line['level']] = msg_type_per_day.get(log_line['level'], 0) + 1

    return msg_type_per_day


def get_max_msg_cnt_in_hour(log_data) -> int:
    '''В какой час было больше всего логов'''

    hours_list = []
    max_hs_cnt = 0
    max_h = 0

    for log_line in log_data:
        hours_list.append(log_line['time'][:2])

    for h, hs in groupby(hours_list):
        hs_cnt = len(list(hs))
        if hs_cnt > max_hs_cnt:
            max_hs_cnt = hs_cnt
            max_h = int(h)

    return max_h


def get_critical_logs():
    '''Сколько логов уровня CRITICAL было в период с 05:00:00 по 05:20:00'''
    grep_pattern = r'"time": "05:([01][0-9]|20:00).*"level": "CRITICAL"'
    full_command = f'''grep -cE '{grep_pattern}' {LOG_FILENAME}'''

    cmd = shlex.split(full_command)
    critical_logs = subprocess.run(cmd, capture_output=True).stdout.decode()
    return critical_logs.strip()


def get_count_logs_with_dog():
    '''Сколько сообщений содержат слово dog'''

    grep_pattern = r'message.*\Wdog\W'
    full_command = f'''grep -cE '{grep_pattern}' {LOG_FILENAME}'''

    cmd = shlex.split(full_command)
    logs_with_dog_count = subprocess.run(cmd, capture_output=True).stdout.decode()
    return logs_with_dog_count.rstrip()


def get_most_common_word_in_warnings(log_data):
    '''Какое слово чаще всего встречалось в сообщениях уровня WARNING'''

    words_dict = {}

    for log_line in log_data:
        if log_line['level'] == 'WARNING':
            words = log_line['message'].split()
            for word in words:
                words_dict[word] = words_dict.get(word, 0) + 1
    most_popular_word = max(words_dict, key=words_dict.get)

    return most_popular_word


if __name__ == '__main__':
    # Десериализуем JSON строки файла с логами
    with open(LOG_FILENAME, encoding='utf-8') as file:
        data = [json.loads(line) for line in file.readlines()]

    msg_type_per_day = get_messages_number_by_type(data)
    hour_max_logs = get_max_msg_cnt_in_hour(data)
    critical_logs = get_critical_logs()
    logs_with_dog = get_count_logs_with_dog()
    most_popular_word = get_most_common_word_in_warnings(data)

    print(
        msg_type_per_day,
        hour_max_logs,
        critical_logs,
        logs_with_dog,
        most_popular_word,
        sep='\n'
        )
