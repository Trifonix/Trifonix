/**
 * Факториал числа  
 * Ввод: целое положительное число `n`  
 * Вывод: `n!`
 */
const number = prompt('Введите целое положительное число');
let factorial = 1;
for (let i = 1; i <= number; i++) {
  factorial *= i;
}
alert(factorial);
