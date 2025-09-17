## Абстрактная фабрика

from abc import ABCMeta, abstractmethod

# ======== ======== #

# Создание абстрактного класса - завод выпускает двигатель (абстрактный метод)
class IEngine(metaclass=ABCMeta):
  @abstractmethod
  def release_engine(self):
    pass

# Реализация интерфейса класса завода (японский и российский двигатели)
class JapaneseEngine(IEngine):
  def release_engine(self):
    print('японский двигатель')

class RussianEngine(IEngine):
  def release_engine(self):
    print('российский двигатель')

# ======== ======== #

# Производство автомобителей
class ICar(metaclass=ABCMeta):
  @abstractmethod
  def release_car(self, engine: IEngine):
    pass

# Реализация абстракции машины через японскую и российскую машины
class JapaneseCar(ICar):
  def release_car(self, engine: IEngine):
    print('Собрали японский автомобиль, ', end='')
    engine.release_engine()
  
class RussianCar(ICar):
  def release_car(self, engine: IEngine):
    print('Собрали российский автомобиль, ', end='')
    engine.release_engine()

# ======== ======== #

# Создание интерфейса фабрики производства автомобилей
class IFactory(metaclass=ABCMeta):
  @abstractmethod
  def create_engine(self) -> IEngine:
    pass
  @abstractmethod
  def create_car(self) -> ICar:
    pass

# Реализация интерфейса фабрики классами японской и российской машин
class JapaneseFactory(IFactory):
  def create_engine(self) -> IEngine:
    return JapaneseEngine()
  
  def create_car(self) -> ICar:
    return JapaneseCar()

class RussianFactory(IFactory):
  def create_engine(self) -> IEngine:
    return RussianEngine()
  
  def create_car(self) -> ICar:
    return RussianCar()

# ======== ======== #

if __name__ == '__main__':
  # Строительство фабрики японских авто
  j_factory = JapaneseFactory()
  j_engine = j_factory.create_engine()
  j_car = j_factory.create_car()

  j_car.release_car(j_engine)

  # Строительство фабрики российских авто
  r_factory = RussianFactory()
  r_engine = r_factory.create_engine()
  r_car = r_factory.create_car()

  r_car.release_car(r_engine)
