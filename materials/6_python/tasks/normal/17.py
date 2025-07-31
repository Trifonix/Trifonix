'''
Поиск самого частого элемента
Ввод: список
Вывод: элемент, встречающийся чаще всего
'''
from collections import Counter
s = input("Вве элементы через пробел: ")
items = s.split()
counts = Counter(items)
most_common = counts.most_common(1)[0][0]
print(most_common)
