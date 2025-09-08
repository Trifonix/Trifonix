// Замыкания - это функция внутри другой функции

// function createCulcFunction(n) {
//   return function () {
//     console.log(1000 * n);
//   };
// }

// const calc = createCulcFunction(42);
// calc();

// function createIncrementor(n) {
//   return function (num) {
//     return n + num;
//   };
// }

// const addOne = createIncrementor(1);
// const addTen = createIncrementor(10);

// console.log(addOne(10));
// console.log(addOne(41));

// console.log(addTen(10));
// console.log(addTen(41));

function urlGenerator(domain) {
  return function(url) {
    return `https://${url}.${domain}`
  }
}

const comUrl = urlGenerator('com');
const ruUrl = urlGenerator('ru');

console.log(comUrl('yandex'));
console.log(comUrl('dzen'));
console.log(comUrl('rambler'));

console.log(ruUrl('google'));
console.log(ruUrl('yahoo'));
