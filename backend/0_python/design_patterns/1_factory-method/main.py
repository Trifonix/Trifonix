# Абстрактный релиз выпуска нового автомобиля
class IProduct:
  def release(self):
    pass

# Создание дочерних классов для реализации интерфейса родительского класса
class Car(IProduct):
  def release(self):
    print('Выпущен новый легковой автомобиль')

class Truck(IProduct):
  def release(self):
    print('Выпущен новый грузовой автомобиль')

# Создание абстрактного автомобильного цеха
class IWorkShop:
  def create(self) -> IProduct:
    pass

# Реализация интерфейса цеха
class CarWorkShop(IWorkShop):
  def create(self):
    return Car() # Возврат экземпляра легкового авто

class TruckWorkShop(IWorkShop):
  def create(self):
    return Truck() # Возврат экземпляра грузового авто

# Инициализация
if __name__ == "__main__":
  creator = CarWorkShop() # Создание экземпляра цеха легковых авто
  car = creator.create() # Создание легкового авто

  creator = TruckWorkShop() # Переквалификация в цех грузовых авто
  truck = creator.create() # Создание грузового авто

  car.release() # Выпуск легкового авто
  truck.release() # Выпуск грузового авто
