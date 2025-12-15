'''
Напишите функцию check_type для проверки,
является ли переданный объект экземпляром класса Animal или его подклассов
Используйте функцию isinstance() для выполнения проверки
Затем создайте классы Animal, Dog, Cat и проверьте несколько объектов
'''

class Animal:
  pass

class Dog(Animal):
  pass

class Cat(Animal):
  pass

class Bird:
  pass

def check_type(obj):
  return isinstance(obj, Animal)

my_dog = Dog()
my_cat = Cat()
my_bird = Bird()

print(check_type(my_dog))
print(check_type(my_cat))
print(check_type(my_bird))
