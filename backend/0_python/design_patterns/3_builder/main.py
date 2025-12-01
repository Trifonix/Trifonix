## Строитель

from abc import ABCMeta

# ======== ======== #

# Создание класса Телефон - производство системы
class Phone:
  def __init__(self):
    self.data: str = ''
  
  def about_phone(self) -> str:
    return self.data
  
  def append_data(self, string: str):
    self.data += string

# ======== ======== #

# Создание интерфейса разработчика Телефона
class IDeveloper(metaclass=ABCMeta):
  def create_display(self):
    pass
  def create_box(self):
    pass
  def system_install(self):
    pass
  def get_phone(self) -> Phone:
    pass

# Создание класса разработчика Android-телефона
class AndroidDeveloper(IDeveloper):
  def __init__(self):
    self.__phone = Phone()
  
  def create_display(self):
    self.__phone.append_data("Произведен дисплей Samsung; ")
  
  def create_box(self):
    self.__phone.append_data("Произведен корпус Samsung; ")
  
  def system_install(self):
    self.__phone.append_data("Установлена система Android; ")
  
  def get_phone(self) -> Phone:
    return self.__phone

# Создание класса разработчика Iphone-телефона
class IphoneDeveloper(IDeveloper):
  def __init__(self):
    self.__phone = Phone()

  def create_display(self):
    self.__phone.append_data("Произведен дисплей Iphone; ")
  
  def create_box(self):
    self.__phone.append_data("Произведен корпус Iphone; ")
  
  def system_install(self):
    self.__phone.append_data("Установлена система IOS; ")
  
  def get_phone(self) -> Phone:
    return self.__phone

# ======== ======== #

# Создание директора для управления разработчиками
class Director:
  def __init__(self, developer: IDeveloper):
    self.__developer = developer

  def set_developer(self, developer: IDeveloper):
    self.__developer = developer
  
  def mount_only_phone(self) -> Phone:
    self.__developer.create_box()
    self.__developer.create_display()
    return self.__developer.get_phone()
  
  def mount_full_phone(self) -> Phone:
    self.__developer.create_box()
    self.__developer.create_display()
    self.__developer.system_install()
    return self.__developer.get_phone()

# ======== ======== #

# Проверка реализации паттерна Строитель
if __name__ == "__main__":
  
  # Создание разработчика на Android платформе
  android_developer: IDeveloper = AndroidDeveloper()

  # Создание директора с передачей созданного разработчика
  director = Director(android_developer)

  # Вызов метода создания телефона у директора
  samsung: Phone = director.mount_full_phone()
  # Вывод информации о созданном телефоне
  print(samsung.about_phone())
  
  # Создание разработчика на Iphone платформе
  iphone_developer: IDeveloper = IphoneDeveloper()

  # Назначение iphone-разработчика в подчинение директору
  director.set_developer(iphone_developer)
  
  # Вызов метода создания телефона без ОС у директора
  iphone: Phone = director.mount_only_phone()
  print(iphone.about_phone())
