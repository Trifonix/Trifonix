/**
 * Количество гласных в строке
 * Ввод: строка
 * Вывод: количество гласных букв (`a`, `e`, `i`, `o`, `u`)
 * Например, pneumonoultramicroscopicsilicovolcanoconiosis - 20 гласных
 */
const string = prompt("Введите строку");
const glasnye = ["a", "e", "i", "o", "u"];
let count = 0;
for (letter of string) {
  for (let i = 0; i < glasnye.length; i++) {
    if ((letter === glasnye[i])) {
      count += 1;
      break;
    }
  }
}
alert(count);
