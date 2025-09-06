'''
Факториал числа 
Ввод: целое положительное число `n`
Вывод: `n!`
'''
N = int(input('Вве число '))
result = 1
for i in range(1, N+1):
  result *= i
print(result)
