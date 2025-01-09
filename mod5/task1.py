from flask import Flask
import subprocess
import os
import signal

PORT_NUMBER = 5000
PID_POS = 1

app = Flask(__name__)

@app.route('/action')
def action():
    return 'Приложение смогло запуститься на нужном порте!'

def lsof_check(port):
    lsof = subprocess.run(['lsof', '-i', f':{port}'], capture_output=True)
    lsof_output_lines = lsof.stdout.decode().splitlines()[1:]

    return list(lsof_output_lines)

def run_app(port):

    pids = []
    lsof_output_lines = lsof_check(port)

    if lsof_output_lines:
        for proc in lsof_output_lines:
            print(pids)
            pids.append(int(proc.split()[PID_POS]))

        if pids:
            [os.kill(pid, signal.SIGKILL) for pid in pids]

    # Повторная проверка отсуствия процессов занявших нужный порт
    if not lsof_check(port):
        app.run(port=port)

if __name__ == '__main__':

    run_app(PORT_NUMBER)

# python3 task1.py &> /dev/null < /dev/null &