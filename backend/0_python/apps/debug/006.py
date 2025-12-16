'''
Напишите функцию complex_operation, 
которая вызывает несколько вложенных функций 
и может вызвать исключение

Если возникает исключение, перехватите его и извлеките "сырые"
сведения о трассировке стека с использованием traceback.extract_tb()

Выведите информацию о каждом фрейме стека (файл, строка, имя функции, текст строки)
'''

import traceback
import sys

def second_func(text):
  return int(text)

def first_func():
  second_func('hello world')

def complex_operation():
  try:
    first_func()
  except:
    tb = sys.exc_info()[2]
    print('Вот мы и попали в исключение!!')
    print('=' * 42)
    for frame in traceback.extract_tb(tb):
      print(f"Файл: {frame.filename}")
      print(f"Линия: {frame.lineno}")
      print(f"Имя функции: {frame.name}")
      print(f"Текст: {frame.line}")
      print('=' * 42)

res = complex_operation()
