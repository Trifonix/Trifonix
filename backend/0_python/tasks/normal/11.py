'''
Сортировка списка
Ввод: список чисел
Вывод: отсортированный список по возрастанию
'''
s = input('Вве числа через пробел: ')
numbers = list(map(int, s.split()))
numbers.sort()
print(numbers)
