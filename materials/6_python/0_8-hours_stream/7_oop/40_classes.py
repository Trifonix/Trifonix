# классы, методы, свойства (атрибуты)
# наследование, инкапсуляция, полиморфизм, (абстракция?)

"""
Инкапсуляция - храните всё внутри и скрыто,
а для взаимодейсвия выдавайте "рычаги" (API)
"""

# Например, есть класс Животное
class Example:
  pass

# У него есть 3 свойства: Имя (str), Возраст (int), Сытость (bool)
class Examplee:
  name = "Имя"
  age = 42
  fed = True

# Теперь можно общаться к свойствам класса
print(Examplee.age)

# Чтобы создавать "животных", нужен конструктор
class Animal:
  name = ""
  age = 0
  fed = False
  count = 0

  def __init__(self, name, age, fed):
    self.name = name
    self.age = age
    self.fed = fed
    Animal.count += 1

  # Метод кормления животного
  def feed(self):
    if not self.fed:
      self.fed = True

# Создаём экземпляр класса Животное
first = Animal('Собака', 2, False)
print(first.name, first.age, first.fed, Animal.count)

# Кормим первое животное
print("Было:", first.fed)
first.feed()
print("Стало:", first.fed)

# __del__ __lt__ __len__
