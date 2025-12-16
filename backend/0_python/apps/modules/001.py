# Импорт элементов из модуля

# Создайте модуль geometry.py, который содержит функции circle_area(radius) и rectangle_area(length, width).
# Затем импортируйте только функцию circle_area и используйте её в другом файле.

from geometry import circle_area

print(circle_area(5))
