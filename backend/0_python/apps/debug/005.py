'''
Напишите функцию divide_numbers, 
которая принимает два аргумента 
и делит первое число на второе

Если возникает исключение ZeroDivisionError,
перехватите его и выведите стек-трейс,
используя модуль traceback.
'''

import traceback

def divide_numbers(x, y):
  try:
    return x / y
  except ZeroDivisionError as e:
    print('Случилось исключение!')
    traceback.print_exc()

result = divide_numbers(4, 0)
print(result)
