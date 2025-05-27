# -------------------------------------
# Задача 4. Перенаправление вывода
import sys
import traceback

class Redirect:

    def __init__(self, stdout = None, stderr = None):

        # Сохраняем текущие потоки вывода и ошибок
        self.base_stdout = sys.stdout
        self.base_stderr = sys.stderr

        self.stdout = stdout
        self.stderr = stderr

    def __enter__(self):

        # Применяем файлы для перенаправления потоков вывода и ошибок
        if self.stdout:
            sys.stdout = self.stdout

        if self.stderr:
            sys.stderr = self.stderr

    def __exit__(self, exc_type, exc_val, exc_tp):

        # Записываем отформатированное сообщение об ошибке
        if exc_type:
            sys.stderr.write(traceback.format_exc())

        # Восстанавливаем сохранённые потоки вывода и ошибок
        sys.stdout = self.base_stdout
        sys.stderr = self.base_stderr

        return True
