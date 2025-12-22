# Итератор для коллекции

# Напишите класс CollectionIterator, который будет итерироваться по произвольной коллекции (список, строка и т.д.).
# Реализуйте методы __iter__ и __next__.

class CollectionIterator():
  def __init__(self, data):
    self.data = data
    self.index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.index >= len(self.data):
      raise StopIteration
    item = self.data[self.index]
    self.index += 1
    return item

my_iterator = CollectionIterator([2,1,4,3,6,5,8,7,9,0])
my_iterator2 = CollectionIterator("Hello World")

for i in my_iterator:
  print(i)

for j in my_iterator2:
  print(j)
