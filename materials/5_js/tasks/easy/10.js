/**
 * Проверка палиндрома (строка)
 * Ввод: строка
 * Вывод: `True`, если строка читается одинаково с обеих сторон
 */
const string = prompt("Введите строку");
const strArray = string.split("");
for (let i = 0; i <= (strArray.length / 2); i++) {
  const j = strArray.length - (i + 1);
  if (strArray[i] === strArray[j]) {
    if (i === j || i+1 === j || i === j+1) {
      alert(true);
      break;
    } 
  } else {
    alert(false);
    break;
  }
}
