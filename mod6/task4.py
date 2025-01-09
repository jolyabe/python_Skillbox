import logging
import json
from itertools import groupby
import subprocess
import shlex

def get_critical_logs():
    command = '''grep -cE '"time": "05:([01][0-9]|20:00).*"level": "CRITICAL"' skillbox_json_messages.log'''
    cmd = shlex.split(command)
    critical_logs = subprocess.run(cmd, capture_output=True).stdout.decode('utf8')
    return critical_logs.strip()


def get_count_logs_with_dog():
    command ="grep -c 'message.*dog' skillbox_json_messages.log"
    cmd = shlex.split(command)
    logs_with_dog_count = subprocess.run(cmd, capture_output=True).stdout.decode('utf8')
    return logs_with_dog_count.strip()

def get_max_msg_cnt_in_hour(log) -> int:

    hours_list = []
    max_hs_cnt = 0
    max_h = 0

    for json_line in log:
        hours_list.append(json_line['time'][:2])

    for h, hs in groupby(hours_list):
        hs_cnt = len(list(hs))
        if hs_cnt > max_hs_cnt:
            max_hs_cnt = hs_cnt
            max_h = int(h)

    return max_h

def main():
    message_type_per_day = {}

    with open('skillbox_json_messages.log', encoding='utf-8') as file:
        data = [json.loads(line) for line in file.readlines()]

    for log in data:
        message_type_per_day[log['level']] = message_type_per_day.get(log['level'], 0) + 1

    hour_max_logs = get_max_msg_cnt_in_hour(data)
    critical_logs = get_critical_logs()
    logs_with_dog = get_count_logs_with_dog()
    words_dict = {}
    for log in data:
        if log['level'] == 'WARNING':
            words = log['message'].split()
            for word in words:
                words_dict[word] = words_dict.get(word, 0) + 1
    most_popular_word = max(words_dict.items(), key=lambda item: item[1])[0]
    print(message_type_per_day, hour_max_logs, critical_logs, logs_with_dog, most_popular_word, sep='\n')


if __name__ == '__main__':
    main()