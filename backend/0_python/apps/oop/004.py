# Полиморфизм
'''
Создать базовый класс Shape с методом area, возвращающим площадь фигуры
Создать дочерние классы Circle и Rectangle, переопределяющие метод area для своей площади
Использовать полиморфизм, чтобы создать список фигур и вычислить их площади
'''
class Shape:
  def area(self):
    raise NotImplementedError("Subclasses should implement this method!")
    
class Circle(Shape):
  def __init__(self, r):
    self.r = r
  def area(self):
    return 3.14 * self.r**2

class Rectangle(Shape):
  def __init__(self, w, h):
    self.w = w
    self.h = h
  def area(self):
    return self.w * self.h

shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
areas = [shape.area() for shape in shapes]

for area in areas:
  print(area)
