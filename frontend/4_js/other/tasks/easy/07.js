/**
 * Переворот строки
 * Ввод:** строка 
 * Вывод:** строка наоборот
 */
const string = prompt('Введите строку');
const newStr = string.split('').reverse().join('');
alert(newStr);
