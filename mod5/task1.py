# -------------------------------------
# Задача 1. Освобождение порта
import subprocess
import os
import signal
from flask import Flask

PORT_NUMBER = 5000
PID_POS = 1

app = Flask(__name__)

@app.route('/')
def index():
    return 'Приложение смогло запуститься на нужном порту!'

def lsof_check(port):
    lsof = subprocess.run(['lsof', '-i', f':{port}'], capture_output=True)
    lsof_output_lines = lsof.stdout.decode().splitlines()[1:]

    return lsof_output_lines

def run_app(port):

    lsof_output_lines = lsof_check(port)

    if lsof_output_lines:
        for proc in lsof_output_lines:
            pid = int(proc.split()[PID_POS])
            os.kill(pid, signal.SIGKILL)

    # Повторная проверка отсутствия процессов занявших нужный порт
    if not lsof_check(port):
        app.run(port=port)


if __name__ == '__main__':
    run_app(PORT_NUMBER)

# python3 task1.py &> /dev/null < /dev/null &
