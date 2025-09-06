'''
Подсчёт количества слов в строке
Ввод: строка
Вывод: количество слов (слова разделены пробелами, без учёта знаков препинания)
'''
import string
s = input("Введите строку: ")
for char in string.punctuation:
  s = s.replace(char, '')
words = s.split()
print(len(words))
