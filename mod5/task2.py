# -------------------------------------
# Задача 2. Удалённое исполнение кода
import subprocess
import shlex
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

app = Flask(__name__)

PROC_OUT_POS = 0
PROC_ERR_POS = 1

class RunCodeForm(FlaskForm):

    code = StringField(validators=[validators.InputRequired()])
    timeout = IntegerField(validators=[validators.InputRequired(),
                                       validators.NumberRange(min=1, max=30)])

def run_code_internal(code, timeout):

    full_command = f'prlimit --nproc=1:1 python3 -c {shlex.quote(code)}'
    proc = subprocess.Popen(shlex.split(full_command),
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    try:
        out, err = proc.communicate(timeout = timeout)

    except subprocess.TimeoutExpired:
        proc.kill()
        out, err = proc.communicate()
        err = b'timeout error'

    return out, err

@app.route('/run', methods=['POST'])
def run():

    form = RunCodeForm()

    if form.validate_on_submit():
        code, timeout = form.code.data, form.timeout.data
        res = run_code_internal(code, timeout)

        if res[PROC_ERR_POS]:
            return f'Output:\n{res[PROC_OUT_POS].decode()} Code execution error: {res[PROC_ERR_POS].decode()}', 400

        return f'{res[PROC_OUT_POS].decode()}', 200

    return f'Invalid input, {form.errors}', 400

if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"]=False
    app.run(debug=True)
