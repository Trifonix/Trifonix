# Перегрузка операторов индексации

# Напишите класс Matrix, который будет представлять двумерную матрицу и поддерживать перегрузку операторов индексации ([]).
# Реализуйте методы __getitem__ и __setitem__.

from random import randint

class Matrix:
  def __init__(self, x, y):
    self.data = []
    for i in range(x):
      temp = []
      for j in range(y):
        temp.append(randint(1,10))
      self.data.append(temp)

  def __getitem__(self, index):
    row, col = index
    return self.data[row][col]

  def __setitem__(self, index, value):
    row, col = index
    self.data[row][col] = value

# Пример использования
matrix = Matrix(3, 3)
matrix[0, 0] = 1
print(matrix[0, 0])  # Вывод: 1
