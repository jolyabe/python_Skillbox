# -------------------------------------
# Задача 5. Максимальное число
import re
from flask import Flask

app = Flask(__name__)

@app.route('/max_number/<path:line>')
def search_max_number(line):
    line_list = line.split('/')
    valid_numbers = all(map(lambda x: re.match(r'^-?\d+\.?\d*$', x), line_list))
    if valid_numbers:
        max_number = max((float(val) for val in line_list))
        # Если дробная часть равна 0, то приводим к целому числу.
        if max_number.is_integer():
            max_number = int(max_number)
        return f'Максимальное число: {max_number}'

    return 'Передано не число'

if __name__ == '__main__':
    app.run(debug=True)
