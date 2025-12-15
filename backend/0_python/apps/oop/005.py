'''
Создать базовый класс Animal с методом make_sound, возвращающим "Ууууууу!"
Создать дочерние классы Dog и Cat, переопределяющие make_sound
Использовать super() для вызова родительского метода
'''
class Animal:
  def make_sound(self):
    return "Ууууууу!"

class Dog(Animal):
  def make_sound(self):
    return super().make_sound() + " Гав-гав!"

class Cat(Animal):
  def make_sound(self):
    return super().make_sound() + " Мяу-мяу!"

dog = Dog()
cat = Cat()

print(dog.make_sound())  # Ууууууу! Гав-гав!
print(cat.make_sound())  # Ууууууу! Мяу-мяу!
