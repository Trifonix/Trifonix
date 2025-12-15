'''
Создать базовый класс Animal с методом speak, возвращающим строку "Ррррр!"
Создать дочерний класс Dog (наследуемый от Animal), переопределяющий метод speak (строка "Гав!")
'''
class Animal():
  def speak(self):
    return "Ррррр!"

class Dog(Animal):
  def speak(self):
    return f"{super().speak()} Гав!"

ani = Animal()
print(ani.speak())

dog = Dog()
print(dog.speak())
