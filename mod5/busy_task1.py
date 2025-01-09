import sys

from flask import Flask


app = Flask(__name__)

@app.route('/some/')
def some():
    return '123'


if __name__ == '__main__':
    app.run(debug=True)

# python3 busy_task1.py &> /dev/null < /dev/null &