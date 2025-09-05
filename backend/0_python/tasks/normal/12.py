'''
Поиск второго по величине числа
Ввод: список чисел
Вывод: второе по величине уникальное число в списке
'''
s = input("Вве числа через пробел: ")
nums = list(map(int, s.split()))
unique_nums = list(set(nums))
unique_nums.sort()
print(unique_nums[-2])
