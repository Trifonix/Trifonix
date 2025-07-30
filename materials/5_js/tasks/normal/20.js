/**
 * Удаление дубликатов из списка
 * Ввод: список
 * Вывод: новый список без повторяющихся значений, сохраняя порядок
 */
function removeDublicates(arr) {
  const result = [];
  const seen = new Set();
  for (let item of arr) {
    if (!seen.has(item)) {
      seen.add(item);
      result.push(item);
    }
  }
  return result;
}
console.log(removeDublicates([1, 2, 2, 3, 1, 4]));
