# Чтобы ограничить доступ к свойству класса - применяют _
class Animal:
  def __init__(self, age):
    self._age = age
  
  # "геттер"
  def get_age(self):
    return self._age
  
  # "сеттер"
  def set_age(self, age):
    self._age = age
  
animal_list = [
  Animal(12),
  Animal(42)
]

# К приватным атрибутам обращаются через "геттер"
for anim in animal_list:
  print(anim.get_age())
# К приватным атрибутам напрямую НЕ обращаются

# Устанавливают новые значения свойствам через "сеттер"
for anim in animal_list:
  anim.set_age(0)
  print(anim.get_age())
  