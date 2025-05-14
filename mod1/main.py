import os
import random
import re
from datetime import datetime, timedelta
from flask import Flask

app = Flask(__name__)

# -------------------------------------
# Задача 1. /hello_world
@app.route('/hello_world')
def hello_world_view():
    return 'Привет, мир!'

# -------------------------------------
# Задача 2. /cars
cars = [
    'Chevrolet',
    'Renault',
    'Ford',
    'Lada'
    ]

@app.route('/cars')
def cars_view():
    return f'{", ".join(cars)}'

# -------------------------------------
# Задача 3. /cats
cats = [
    'корниш-рекс',
    'русская голубая',
    'шотландская вислоухая',
    'мейн-кун',
    'манчкин'
    ]

@app.route('/cats')
def cats_view():
    choice = random.choice(cats)
    return f'{choice}'

# -------------------------------------
# Задача 4. /get_time/now
@app.route('/get_time/now')
def get_time_now_view():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H-%M-%S')
    return f'Точное время: {current_time}'

# -------------------------------------
# Задача 5. /get_time/future
@app.route('/get_time/future')
def get_time_future_view():
    current_datetime = datetime.now()
    delta = timedelta(hours=1)
    future_datetime = current_datetime + delta
    future_time = future_datetime.strftime('%H-%M-%S')
    return f'Точное время через час будет: {future_time}'

# -------------------------------------
# Задача 6. /get_random_word
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
words = []

def make_words():
    with open(BOOK_FILE, encoding='utf-8') as file:
        text = file.read()
        global words
        words = re.findall(r'\b[a-zA-Zа-яА-Я]+\b', text)


@app.route('/get_random_word')
def get_random_word_view():
    if not words:
        make_words()
    word_random = random.choice(words)
    return f'{word_random}'

# -------------------------------------
# Задача 7. /counter
@app.route('/counter')
def counter():
    counter.visits += 1

    return f'{counter.visits}'

if __name__ == '__main__':
    counter.visits = 0
    app.run(debug=True)
