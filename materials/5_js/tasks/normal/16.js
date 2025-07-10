/**
 * Проверка на анаграмму
 * Ввод: две строки
 * Вывод: `True`, если одна строка является анаграммой другой (например, `"listen"` и `"silent"`)
 */
const str1 = "кабан";
const s1 = str1.split("");
const str2 = "яанка";
let s2 = str2.split("");

if (s1.length === s2.length) {
  for (let i = 0; i < s1.length; i++) {
    for (let j = 0; j < s2.length; j++) {
      if (s1[i] === s2[j]) {
        s2.splice(j, 1);
        if (s2.length === 0) {
          alert(true);
        }
        break;
      }
    }
    if (i === s1.length - 1 && s2.length !== 0) {
      alert(false);
    }
  }
} else {
  alert(false);
}
