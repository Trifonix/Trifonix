/**
 * Поиск самого частого элемента
 * Ввод: список
 * Вывод: элемент, встречающийся чаще всего
 */
const listing = [42, 'chat', 'chat', "apple", 7, "chat", 7, "world", 3.14, "banana", 7, "chat"];
let counter = 0;
let elWithMaxCounter = { el: listing[0], counter: 0 };
for (el of listing) {
  for (let i = 0; i < listing.length; i++) {
    if (el === listing[i]) {
      counter++;
    }
  }
  if (elWithMaxCounter.counter < counter) {
    elWithMaxCounter.el = el;
    elWithMaxCounter.counter = counter;
  }
  counter = 0;
}
alert(elWithMaxCounter.el); // chat - 4 times
