'''
Сумма всех чисел от 1 до N
Ввод: число `n`
Вывод: сумма всех чисел от `1` до `n`
'''
n = int(input("Введите число: "))
total = 0
for i in range(1, n+1):
  total += i
print(total)
