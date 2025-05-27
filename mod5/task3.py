# -------------------------------------
# Задача 3. Заглушка исключений
class BlockErrors():

    def __init__(self, errors):
        self.errors = errors

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, tuple(self.errors))
