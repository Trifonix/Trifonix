# Наследование - один класс наследует свойства и методы другого

class Animal:
  def __init__(self, age):
    self.age = age
  
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, value):
    self._age = value*2

class Dog(Animal):
  def __init__(self, age, walks):
    Animal.__init__(self, age)
    self.walks = walks

class Cat(Animal):
  def __init__(self, age, count_mice):
    Animal.__init__(self, age)
    self.count_mice = count_mice

zhuchka = Dog(4, 2)
barsik = Cat(2, 10)

for x in dir(zhuchka):
  print(x)

for x in dir(barsik):
  print(x)

print(zhuchka.age)
print(barsik.age)
