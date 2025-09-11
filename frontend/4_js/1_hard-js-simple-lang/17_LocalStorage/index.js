const myNumber = 42;

// console.log(localStorage.getItem("number"));
// localStorage.setItem("number", myNumber.toString());
// localStorage.removeItem("number");
// console.log(localStorage.getItem("number"));
// localStorage.clear()

const object = {
  name: "Neo",
  age: 29,
};

// localStorage.setItem("person", object);
// localStorage.setItem("person", JSON.stringify(object));

const raw = localStorage.getItem("person");
const person = JSON.parse(raw);
person.name = "Jack";

// console.log(typeof JSON.parse(raw));
// console.log(JSON.parse(raw));
// console.log(raw);

console.log(person);

// ========
window.addEventListener("storage", (event) => {
  console.log(event);
});

// window.onstorage = () => {};

// Чем отличается LocalStorage от Cookie ?
// 1) LocalStorage больше по объёму (5 мегабайт локально в браузере)
// 2) Cookie улетают с запросами на сервер, а LS - нет
