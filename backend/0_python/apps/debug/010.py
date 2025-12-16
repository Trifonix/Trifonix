# Иерархия пользовательских исключений

# Создайте базовый класс исключений ApplicationError и два подкласса NegativeValueError и ValueTooLargeError.
# Реализуйте функцию check_number, которая будет вызывать соответствующее исключение, если число отрицательное или слишком большое.
# Обработайте исключения в блоке try-except.

class ApplicationError(Exception):
  pass

class NegativeValueError(ApplicationError):
  pass

class ValueTooLargeError(ApplicationError):
  pass

def check_number(number):
  try:
    if number < 0:
      raise NegativeValueError("Негатив")
    elif number > 99:
      raise ValueTooLargeError("Огромное")
  except ApplicationError as e:
    print(e)

check_number(5)
check_number(-1)
check_number(100)
