# -------------------------------------
# Задача 6. Список доступных страниц
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Главная страница'

@app.route('/hello_world')
def hello_world_view():
    return 'Привет, мир!'

cars = [
    'Chevrolet',
    'Renault',
    'Ford',
    'Lada'
    ]

@app.route('/cars')
def cars_view():
    return f'{", ".join(cars)}'

@app.errorhandler(404)
def error_handler(error):
    base_url = 'http://localhost:5000'

    available_urls = [f'<a href="{base_url+url.rule}">'+base_url+url.rule+'</a>'
                      for url in app.url_map.iter_rules()][1:]

    return 'Страница не найдена. Доступные страницы:<br>' + '<br>'.join(available_urls)

if __name__ == '__main__':
    app.run(debug=True)
