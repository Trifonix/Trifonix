/**
 * Сумма всех чисел от 1 до N
 * Ввод: число `n`
 * Вывод: сумма всех чисел от `1` до `n`
 */
const num = prompt('Введите число N');
let sum = 0;
for (let i = 1; i <= num; i++) {
  sum += i;
}
alert(sum);
