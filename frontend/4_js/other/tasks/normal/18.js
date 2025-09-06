/**
 * Генерация списка простых чисел до N
 * Ввод: число `n`
 * Вывод: список всех простых чисел до `n` включительно
 * Используй алгоритм `решето Эратосфена`
 */
const N = +prompt("Вве число");
let arr = new Array(N).fill(1).map((a, i) => i);
let i = 2;
while (i <= N) {
  if (arr[i] !== 0) {
    let j = i + i;
    while (j <= N) {
      arr[j] = 0;
      j = j + i;
    }
  }
  i += 1;
}
arr = arr.filter(num => num !== 0);
arr.shift();
console.log(arr);
