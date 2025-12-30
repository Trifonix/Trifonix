# Исправляем глобальные переменные.

# Исправьте код функции:

x = 10

def foo_correct():
    global x
    x += 1
    print(x)

foo_correct()  # Вывод: 11
