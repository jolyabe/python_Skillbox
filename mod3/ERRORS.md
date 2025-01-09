# Результаты тестирования и исправления ошибок класса Person
## Тестирование №1 и исправление ошибок
### Лог тестирования №1:
```
test_get_address (task4.TestPersonClass) ... ok
test_get_age (task4.TestPersonClass) ... ERROR
test_get_name (task4.TestPersonClass) ... ok
test_is_homeless_1 (task4.TestPersonClass) ... ERROR
test_is_homeless_2 (task4.TestPersonClass) ... ERROR
test_set_address (task4.TestPersonClass) ... FAIL
test_set_name (task4.TestPersonClass) ... FAIL

======================================================================
ERROR: test_get_age (task4.TestPersonClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/arsha/github-repo/skillbox-python-advanced/venv/lib/python3.10/site-packages/freezegun/api.py", line 885, in wrapper
    result = func(*args, **kwargs)
  File "/home/arsha/github-repo/skillbox-python-advanced/module3/task4.py", line 14, in test_get_age
    self.assertEqual(self.person.get_age(), 24)
  File "/home/arsha/github-repo/skillbox-python-advanced/module3/Person.py", line 8, in get_age
    now = datetime.datetime.now()
NameError: name 'datetime' is not defined

======================================================================
ERROR: test_is_homeless_1 (task4.TestPersonClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/arsha/github-repo/skillbox-python-advanced/module3/task4.py", line 36, in test_is_homeless_1
    self.assertFalse(self.person.is_homeless())
  File "/home/arsha/github-repo/skillbox-python-advanced/module3/Person.py", line 27, in is_homeless
    return address is None
NameError: name 'address' is not defined

======================================================================
ERROR: test_is_homeless_2 (task4.TestPersonClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/arsha/github-repo/skillbox-python-advanced/module3/task4.py", line 41, in test_is_homeless_2
    self.assertTrue(self.person.is_homeless())
  File "/home/arsha/github-repo/skillbox-python-advanced/module3/Person.py", line 27, in is_homeless
    return address is None
NameError: name 'address' is not defined

======================================================================
FAIL: test_set_address (task4.TestPersonClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/arsha/github-repo/skillbox-python-advanced/module3/task4.py", line 28, in test_set_address
    self.assertEqual(self.person.get_address(), 'Moscow')
AssertionError: 'Yekaterinburg' != 'Moscow'
- Yekaterinburg
+ Moscow


======================================================================
FAIL: test_set_name (task4.TestPersonClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/arsha/github-repo/skillbox-python-advanced/module3/task4.py", line 23, in test_set_name
    self.assertEqual(self.person.get_name(), 'Ivan Ivanov')
AssertionError: 'Anton Antonov' != 'Ivan Ivanov'
- Anton Antonov
+ Ivan Ivanov


----------------------------------------------------------------------
Ran 7 tests in 0.009s

FAILED (failures=2, errors=3)
```

### Исправление ошибок по результатам тестирования №1:

1. **ERROR: test_get_age (task4.TestPersonClass)** - импортирован модуль `datetime`;
2. **ERROR: test_is_homeless_1 (task4.TestPersonClass)** - ошибочное обращение к переменной `address` заменено на `self.address`;
3. **ERROR: test_is_homeless_2 (task4.TestPersonClass)** - см п.2;
4. **FAIL: test_set_address (task4.TestPersonClass)** - ошибочная операция сравнения `==` заменена на операцию присваивания `=`;
5. **FAIL: test_set_name (task4.TestPersonClass)** - ошибочное присваивание `self.name = self.name` заменено на `self.name = name`.

## Тестирование №2 и исправление ошибок
### Лог тестирования №2:
```
test_get_address (task4.TestPersonClass) ... ok
test_get_age (task4.TestPersonClass) ... FAIL
test_get_name (task4.TestPersonClass) ... ok
test_is_homeless_1 (task4.TestPersonClass) ... ok
test_is_homeless_2 (task4.TestPersonClass) ... FAIL
test_set_address (task4.TestPersonClass) ... ok
test_set_name (task4.TestPersonClass) ... ok

======================================================================
FAIL: test_get_age (task4.TestPersonClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/arsha/github-repo/skillbox-python-advanced/venv/lib/python3.10/site-packages/freezegun/api.py", line 885, in wrapper
    result = func(*args, **kwargs)
  File "/home/arsha/github-repo/skillbox-python-advanced/module3/task4.py", line 14, in test_get_age
    self.assertEqual(self.person.get_age(), 24)
AssertionError: -24 != 24

======================================================================
FAIL: test_is_homeless_2 (task4.TestPersonClass)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/arsha/github-repo/skillbox-python-advanced/module3/task4.py", line 41, in test_is_homeless_2
    self.assertTrue(self.person.is_homeless())
AssertionError: False is not true

----------------------------------------------------------------------
Ran 7 tests in 0.008s

FAILED (failures=2)

```

### Исправление ошибок по результатам тестирования №2:

1. **FAIL: test_get_age (task4.TestPersonClass)** - ошибочный порядок операндов `self.yob - now.year` заменён на `now.year - self.yob`;
2. **FAIL: test_is_homeless_2 (task4.TestPersonClass)** - ошибочная операция `self.address is None` заменена на `self.address == ''`.

## Тестирование №3 и исправление ошибок
### Лог тестирования №3:
```
test_get_address (task4.TestPersonClass) ... ok
test_get_age (task4.TestPersonClass) ... ok
test_get_name (task4.TestPersonClass) ... ok
test_is_homeless_1 (task4.TestPersonClass) ... ok
test_is_homeless_2 (task4.TestPersonClass) ... ok
test_set_address (task4.TestPersonClass) ... ok
test_set_name (task4.TestPersonClass) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.008s

OK
```
### Исправление ошибок по результатам тестирования №3:
***Ошибок нет. Все предыдущие ошибки исправлены.***