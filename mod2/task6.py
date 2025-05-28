# -------------------------------------
# Задача 6. Превью файла
from flask import Flask
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):

    abs_path = os.path.join(BASE_DIR, relative_path)

    try:
        with open(abs_path, encoding='utf-8') as file:
            result_text = file.read(size)
            result_size = len(result_text)

    except FileNotFoundError:
        return 'file not found'

    return f'<b>{abs_path}</b> {result_size}<br>{result_text}'


if __name__ == "__main__":
    app.run(debug=True)
