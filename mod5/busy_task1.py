# -------------------------------------
# Задача 1. Освобождение порта (вспомогательная программа)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '123'


if __name__ == '__main__':
    app.run(debug=True)

# python3 busy_task1.py &> /dev/null < /dev/null &
