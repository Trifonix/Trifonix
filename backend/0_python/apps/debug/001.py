'''
Напишите функцию safe_division, которая принимает два числа и выполняет их деление
Обработайте исключения, которые могут возникнуть при делении на ноль
и при передаче некорректных значений (например, строки вместо чисел)
Функция должна возвращать сообщение об ошибке или результат деления
'''

def safe_division(one, two):
  try:
    return one / two
  except ZeroDivisionError:
    return 'Нельзя на 0 делить!'
  except TypeError:
    return 'Переданы неправильные значения!!'

print(safe_division(4, 2))
print(safe_division(4, 0))
print(safe_division('', 0))
