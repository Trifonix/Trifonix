'''
Создайте два базовых класса BaseA и BaseB, каждый из которых имеет метод action()
Создайте производный класс Derived с переопределенным методом action(),
который вызывает метод super().action()
Вызовите метод action() у объекта класса Derived
и проанализируйте порядок вызова методов
'''

class BaseA:
  def action(self):
    print('I am from Base A')

class BaseB:
  def action(self):
    print('I am from Base B')

class Derived(BaseA, BaseB):
  def action(self):
    super().action()

der = Derived()
der.action()
