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
  console.log("TimeOut!");
}, 2500);

setTimeout(function () {
  greet2(name);
}, 3000);

// clearTimeout

setInterval(function () {
  console.log(911);
}, 2000);

setInterval(function () {
  console.log(Math.random());
}, 2100);

let counter = 0;
const interval = setInterval(function () {
  if (counter === 5) {
    console.log("it was 5");
    clearInterval(interval);
  } else {
    console.log(++counter);
  }
}, 1000);

let counter2 = 0;
const interval2 = setInterval(function () {
  console.log(++counter2);
}, 2500);

// Arrow Functions
function greet(name) {
  console.log('Hello - ', name);
}
const arrow = (name, age) => {
  console.log('Hello - ', name, age);
}

arrow('Megauser', 25);

const name2 = 'hacker';
const arrow2 = (name2) => console.log('qhello, ', name2);
arrow2(name2);

function pow2(num, exp) {
  return Math.pow(num, exp);
}
console.log(pow2(2, 3));

const pow3 = (num, exp) => Math.pow(num, exp);
console.log(pow3(2, 4));

// ======== Default Parameters
const sum = (a = 20, b = a / 2) => a + b;
console.log(sum(40, 2));
console.log(sum(40));

// остаточный параметр rest
function sumAll( ... numbers ) {
  //console.log(numbers);
  // let res = 0;
  // for (let num of numbers) {
  //   res += num;
  // }
  // return res;
  return numbers.reduce((acc, cur) => acc += cur, 0);
}
console.log('sum was ===', sumAll(1, 2, 3, 4, 5, 6));

// Closures - Замыкания
function createPerson(name) {
  return function(lastName) {
    console.log(name + ' ' + lastName);
  }
}
const addLastName = createPerson('agent');
addLastName('Smith');
addLastName('Neo');
