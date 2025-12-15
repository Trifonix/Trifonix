'''
Создайте классы A, B, C, и D, где B и C наследуют от A, а D наследует от B и C.
В каждом классе определите метод method, 
который выводит имя класса и вызывает метод super().method().
'''
class A:
  def method(self):
    print('я A')

class B(A):
  def method(self):
    print('я B')
    super().method()

class C(A):
  def method(self):
    print('я C')
    super().method()

class D(B, C):
  def method(self):
    print('я D')
    super().method()

my_d = D()
my_d.method()
