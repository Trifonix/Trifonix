function calcValues(a, b) {
  return [a + b, a - b, a * b, a / b];
  // return [a + b, undefined, a * b, a / b];
}

// console.log(calcValues(42, 10));

// const [sum, sub] = calcValues(52, 10);
// const [sum, , mul, ...other] = calcValues(52, 10);
const [sum, sub = "Вычитания нет", mul, ...other] = calcValues(52, 10);
// const sum = result[0];
// const sub = result[1];
// const [sum, sub] = result

// console.log(sum, sub);
// console.log(sum, mul, other, sub);

// ======== Objects
const person = {
  name: "John",
  age: 20,
  address: {
    country: "USA",
    city: "NY",
  },
};

// const name = person.name;
// const {
//   name: firstName = "Имени нет",
//   age,
//   car = "Машины нет",
//   address: { city: homeTown, country },
// } = person;

const { name, ...info } = person;

// console.log(firstName, age, car, homeTown, country);
// console.log(name, info);

function logPerson({name: firstName = 'qwe', age}) {
  console.log(firstName + " " + age);
}

logPerson(person);
