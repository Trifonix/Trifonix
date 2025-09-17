'''
Проверка сбалансированности скобок
Ввод: строка из скобок: `()[]{}`
Вывод: `True`, если скобки правильно сбалансированы
'''
def is_balanced(s):
  stack = []
  pairs = {')': '(', ']': '[', '}': '{'}
  for char in s:
    if char in '([{':
      stack.append(char)
    elif char in ')]}':
      if not stack or stack[-1] != pairs[char]:
        return False
      stack.pop()
  return len(stack) == 0
s = input('Вве строку со скобками: ')
print(is_balanced(s))
