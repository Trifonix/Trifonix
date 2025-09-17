import math

class Figure:
  def __init__(self):
    pass

  def get_area(self):
    pass

  def get_perimetr(self):
    pass

class Square(Figure):
  def __init__(self, a):
    self.a = a

  def get_area(self):
    return self.a * self.a
  
  def get_perimetr(self):
    return self.a * 4
  
class Triangle(Figure):
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def get_area(self):
    p = (self.a+self.b+self.c)/2
    return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
  
  def get_perimetr(self):
    return self.a + self.b + self.c
