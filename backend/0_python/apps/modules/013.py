# Параметры по умолчанию.

# Напишите 2 функции: def foo(bar=[]) и foo_correct(bar=None).
# Каждая функция принимает список и добавляет в него элемент "baz".
# Если список не передан, функция должна использовать новый пустой список.
# Покажите, как использование изменяемого объекта в качестве значения по умолчанию может привести к неожиданному поведению, и исправьте это (во второй функции).

def foo(bar=[]):
  bar.append("baz")
  return bar

def foo_correct(bar=None):
  if bar is None:
    bar = []
  bar.append("baz")
  return bar

# foo не работает
print(foo()) # Выводит: ['baz']
print(foo()) # Выводит: ['baz', 'baz']

# Проверка исправленной функции
print(foo_correct())  # Выводит: ['baz']
print(foo_correct())  # Выводит: ['baz']
print(foo_correct())  # Выводит: ['baz']

# Проверка с передачей списка
lst = [1, 2, 3]
print(foo_correct(lst))  # Выводит: [1, 2, 3, "baz"]
print(foo_correct(lst))  # Выводит: [1, 2, 3, "baz", "baz"]