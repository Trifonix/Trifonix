/**
 * Является ли число простым
 * Ввод: целое положительное число
 * Вывод: `True` или `False`
 */
const num = +prompt('Введите число, проверить простое ли оно');
for (let i = 2; i <= num; i++) {
  if (num % i === 0) {
    if (num === i) {
      alert(true);
      break;
    }
    alert(false);
    break;
  } else {
    if (i !== num) {
      continue;
    }
  }
}
