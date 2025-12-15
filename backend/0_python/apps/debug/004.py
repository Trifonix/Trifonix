'''
Напишите функцию read_integer, которая принимает строку и пытается преобразовать её в целое число
Если возникает ValueError, обработайте исключение и выведите аргументы ошибки и тип ошибки
Дополнительно, сохраните исключение в переменной и выведите её за пределами блока except
'''

def read_integer(stringing):
  try:
    print(int(stringing))
  except ValueError as e:
    global exception
    exception = e
    print(f"Аргументы: {e.args}\nТип: {type(e)}")
  
read_integer('qwe')
print(exception)
