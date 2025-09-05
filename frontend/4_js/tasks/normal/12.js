/**
 * Поиск второго по величине числа
 * Ввод: список чисел
 * Вывод: второе по величине уникальное число в списке
 */
const nums = [1, 12, 6, 4, 5, 77, 0, 5, 4];
const maxNum = Math.max(...nums);
const maxNumIndex = nums.indexOf(maxNum);
nums.splice(maxNumIndex, 1);
const preMaxNum = Math.max(...nums);
alert(preMaxNum);
