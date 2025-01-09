from flask import Flask

app = Flask(__name__)

storage = {}

@app.route('/add/<date>/<int:number>')
def add(date: str, number: int) -> str:

    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:8])
    storage.setdefault(year, {'total': 0}).setdefault(month, {'total': 0}).setdefault(day, 0)
    storage[year][month][day] += number
    storage[year][month]['total'] += number
    storage[year]['total'] += number
    return 'Данные записаны'

@app.route('/calculate/<int:year>')
def calculate_year(year: int) -> str:
    try:
        result = storage[year]['total']
        return f'{result}'
    except KeyError:
        return f'Нет данных за {year} год.'

@app.route('/calculate/<int:year>/<int:month>')
def calculate_year_month(year: int, month: int) -> str:
    try:
        result = storage[year][month]['total']
        return f'{result}'
    except KeyError:
        return f'Нет данных за {year} год и {month} месяц.'

if __name__ == '__main__':

    app.run(debug=True)
