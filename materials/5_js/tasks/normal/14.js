/**
 * Подсчёт количества слов в строке
 * Ввод: строка
 * Вывод: количество слов (слова разделены пробелами, без учёта знаков препинания)
 */
const str = prompt("Введите строку текста");
// SEO-анализ текста от Text.ru - это уникальный сервис, не имеющий аналогов. Возможность подсветки «воды», заспамленности и ключей в тексте позволяет сделать анализ текста интерактивным и легким для восприятия.
const newStr = str.split(' ');
// 28 слов
alert(newStr.length);
