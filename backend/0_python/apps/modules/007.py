# Использование пакета requests.

# Используйте пакет requests для выполнения GET-запроса к API.
# Выполните следующие шаги:
# Установите пакет requests с помощью pip.
# pip install requests
# Используйте пакет requests для выполнения GET-запроса к API, 
# например, к https://jsonplaceholder.typicode.com.
import requests
r = requests.get('https://jsonplaceholder.typicode.com', auth=('user', 'pass'))
print(r.text)

# print(r)
# print(r.status_code)
# print(dir(r))
# print(r.headers['content-type'])
# r.json()

# Выведите на экран результат запроса.
'''
<!DOCTYPE html>
<html lang="en">
  <head>
'''
