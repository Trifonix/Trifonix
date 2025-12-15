'''
Создать базовый класс Vehicle со свойствами brand и model
Создать дочерний класс Car (наследование от Vehicle) и добавить свойство fuel_type
Использовать функцию super()
'''

class Vehicle():
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

class Car(Vehicle):
  def __init__(self, brand, model, fuel_type):
    super().__init__(brand, model)
    self.fuel_type = fuel_type

my_car = Car('Audi', 'V8', 'gas')
print(my_car.brand)
print(my_car.model)
print(my_car.fuel_type)
