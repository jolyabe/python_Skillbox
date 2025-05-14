# -------------------------------------
# Задача 1. Список процессов
RSS_POS = 5

def get_summary_rss(file_path):
    with open(file_path, encoding='utf-8') as file:
        total_bytes = 0
        for line in file.readlines()[1:]:
            splitted_line = line.split()
            rss_value = splitted_line[RSS_POS]
            total_bytes += int(rss_value)

        total_kb = total_bytes // 1024
        total_mb = total_kb // 1024
        print(f"{total_bytes} B, {total_kb} KiB, {total_mb} MiB")


if __name__ == '__main__':
    path_to_file = 'output_file.txt'
    get_summary_rss(path_to_file)
