# Перегрузка операторов сравнения

# Напишите класс Person, который будет представлять человека с атрибутами name и age.
# Реализуйте перегрузку операторов сравнения == и < для сравнения людей по возрасту.

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __eq__(self, other):
    return self.age == other.age
  
  def __lt__(self, other):
    return self.age < other.age

p1 = Person('Neo', 28)
p2 = Person('Smith', 32)

print(p1==p2)
print(p1<p2)
