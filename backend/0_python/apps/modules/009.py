# Создание простого итератора

# Напишите класс SimpleIterator,
# который будет итерироваться по последовательности чисел от start до end
# Реализуйте методы __iter__ и __next__

class SimpleIterator():
  def __init__(self, start, end):
    self.index = start
    self.end = end

  def __iter__(self):
    return self

  def __next__(self):
    if self.index >= self.end:
      raise StopIteration
    current = self.index
    self.index += 1
    return current

item = SimpleIterator(1, 5)
for number in item:
  print(number)
