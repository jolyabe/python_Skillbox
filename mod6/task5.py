from datetime import datetime, timedelta
import re

LOG_FILENAME = 'measure_me.log'

def get_measure_me_average_time_delta() -> int:

    entry_messages: list[str] = []
    leave_messages: list[str] = []
    time_delta_sum = 0
    message_cnt = 0

    with open('measure_me.log', 'r') as file:

        for line in file.readlines():
            if re.search(r'.*Enter measure_me$', line):
                entry_messages.append(line.rstrip())
            if re.search(r'.*Leave measure_me$', line):
                leave_messages.append(line.rstrip())

    zipped_data = zip(entry_messages, leave_messages)

    for e, l in zipped_data:

        e_time = datetime.strptime(e[:9], '%M:%S.%f')
        l_time = datetime.strptime(l[:9], '%M:%S.%f')
        time_delta = (l_time - e_time).total_seconds()
        time_delta_sum += time_delta
        message_cnt += 1

    average_time_delta = time_delta_sum / message_cnt

    return average_time_delta

if __name__ == '__main__':

    print(f'Среднее время исполнения measure_me() = {get_measure_me_average_time_delta():.3f} с.')