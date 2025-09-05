/**
 * Проверка сбалансированности скобок
 * Ввод: строка из скобок: `()[]{}`
 * Вывод: `True`, если скобки правильно сбалансированы
 */
function isBalanced(str) {
  const stack = [];
  const pairs = {
    ")": "(",
    "]": "[",
    "}": "{",
  };
  for (let char of str) {
    if (char === "(" || char === "[" || char === "{") {
      stack.push(char);
    } else if (char === ")" || char === "]" || char === "}") {
      if (stack.pop() !== pairs[char]) {
        return false;
      }
    }
  }
  return stack.length === 0;
}
console.log(isBalanced("([{}])")); // true
console.log(isBalanced("([)]))")); // false
