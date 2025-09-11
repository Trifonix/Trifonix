const citiesRussian = ["Москва", "СПб", "Казань", "Новосиб"];
const citiesEurope = ["Лондон", "Прага", "Париж"];

const citiesRussianWithPopulation = {
  Moscow: 20,
  SPb: 8,
  Kazan: 5,
  Novosib: 3,
};
const citiesEuropeWithPopulation = {
  Moscow: 26,
  London: 10,
  Praha: 3,
  Paris: 2,
};

// Spread
// console.log(citiesRussian);
// console.log(...citiesRussian);
// console.log(...citiesEurope);

// const allCities = [...citiesEurope, 'Вашингтон', ...citiesRussian];
// const allCities = citiesEurope.concat(citiesRussian);
// console.log(allCities);

// console.log(citiesRussianWithPopulation);
// console.log({...citiesRussianWithPopulation});
// console.log({ ...citiesRussianWithPopulation, ...citiesEuropeWithPopulation });
// console.log({ ...citiesEuropeWithPopulation, ...citiesRussianWithPopulation });

// ======== Practice
const numbers = [5, 37, 42, 17];
// console.log(Math.max(...numbers));
// console.log(Math.max.apply(null, numbers));

const divs = document.querySelectorAll("div");
const nodes = [...divs];
// console.log(divs);
// console.log(divs.forEach());
// console.log(divs.map());
// console.log(divs, Array.isArray(divs));
// console.log(nodes, Array.isArray(nodes));

// Rest
function sum(a, b, ...rest) {
  // console.log(rest);
  return a + b + rest.reduce((a, i) => a + i, 0);
}

const nums = [1, 2, 3, 4, 5, 6, 7, 8];

// Spread !!
// console.log(sum(...nums));

// const a = nums[0];
// const b = nums[1];
// console.log(a, b);

// Деструктуризация
const [a, b, ...other] = nums;
console.log(a, b, other);

const person = {
  name: "Neo",
  age: 28,
  city: "NY",
  country: "USA",
};

const { name, age, ...address} = person;

console.log(name, age, address);
