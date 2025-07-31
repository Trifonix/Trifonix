'''
Сумма чисел на чётных позициях
Ввод: список чисел
Вывод: сумма чисел на индексах 0, 2, 4 и т. д.
'''
s = input("Вве числа через пробел: ")
numbers = list(map(int, s.split()))
total = 0
for i in range(0, len(numbers), 2):
  total += numbers[i]
print(total)
