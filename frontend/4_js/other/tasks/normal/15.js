/**
 * Сжатие строки (Run Length Encoding)
 * Ввод: строка, например `aaabbbcc`
 * Вывод: сжатая форма, например `a3b3c2`
 */
const str = "wwwwaaadexxxxxx";
const arr = str.split("");
let newStr = '';
let tempLetter = arr[0];
let counter = 0;
newStr += arr[0];
let lastElement = arr.length;
for (letter of arr) {
  lastElement--;
  if (letter === tempLetter) {
    counter++;
    if (lastElement===0) {
      newStr += counter;
    }
  } else {
    newStr += counter;
    tempLetter = letter;
    counter = 1;
    newStr += letter;
    continue;
  }
}
alert(newStr); // w4a3d1e1x6
