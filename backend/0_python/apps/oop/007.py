'''
Напишите функцию check_subclass для проверки, является ли один класс подклассом другого.
Используйте функцию issubclass() для выполнения проверки.
Затем создайте классы Vehicle, Car, Bicycle, и проверьте, являются ли Car и Bicycle подклассами Vehicle.
'''

class Vehicle:
  pass

class Car(Vehicle):
  pass

class Bicycle:
  pass

def check_subclass(sub, sup):
  return issubclass(sub, sup)

print(check_subclass(Car, Vehicle))
print(check_subclass(Bicycle, Vehicle))
