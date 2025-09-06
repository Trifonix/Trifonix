'''
Количество гласных в строке
Ввод: строка
Вывод: количество гласных букв (`a`, `e`, `i`, `o`, `u`)
Например, pneumonoultramicroscopicsilicovolcanoconiosis - 20 гласных
'''
s = input("Введите строку: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
count = 0
for char in s.lower():
  if char in vowels:
    count += 1
print(count)
