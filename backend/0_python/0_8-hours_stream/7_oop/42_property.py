# Вообще инкапсуляция с "геттерами" и "сеттерами" используется в иных языках (?)
# В Питоне используют property (декораторы)

class Animal:
  def __init__(self, name):
    self._name = name
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, value):
    self._name = value.upper()

first = Animal("John")
print(first.name)

first.name = "Smith"
print(first.name)
