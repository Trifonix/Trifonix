# Пользовательское исключение

# Создайте пользовательское исключение InvalidAgeError, которое будет вызываться в функции check_age,
# если возраст меньше 0 или больше 150. Обработайте это исключение в блоке try-except.

class InvalidAgeError(Exception):
  pass

def check_age(age):
  if age < 0:
    raise InvalidAgeError("Возраст меньше 0")
  elif age > 150:
    raise InvalidAgeError("Возраст больше 150")

try:
  age = int(input("Enter your age: "))
  check_age(age)
  print("Age is valid.")
except InvalidAgeError as e:
  print(e)
except ValueError:
  print("Please enter a valid integer for age.")
