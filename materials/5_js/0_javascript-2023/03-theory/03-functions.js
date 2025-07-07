// Function Declaration
const name = "user";
function greet(name) {
  console.log("Hello,", name, "!");
}
greet(name);

// Function Expression
const greet2 = function (name) {
  console.log("2 Hello", name);
};
greet2("Smith");
// FE не будет работать
// если вызов FE до декларации FE

console.log(typeof greet);
console.log(typeof greet2);

console.dir(greet);
console.dir(greet2);

console.dir(greet2.toString());

// setInterval
// setTimeout
setTimeout(greet, 1500);

setTimeout(function () {
  console.log('TimeOut!');
}, 2500);
