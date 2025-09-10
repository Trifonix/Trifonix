const people = [
  { name: "Neo", age: 28, budget: 42000 },
  { name: "Smith", age: 33, budget: 82000 },
  { name: "Trinity", age: 19, budget: 12000 },
  { name: "Morpheus", age: 35, budget: 55042 },
];

// ======== ES5
// for (let i = 0; i < people.length; i++) {
//   console.log(people[i]);
// }

// ======== ES6
// for (let person of people) {
//   console.log("For-Of");
//   console.log(person);
// }

// ======== forEach
// people.forEach(function (person, index, pArr) {
//   console.log(person);
//   console.log(index);
//   console.log(pArr);
// });

// people.forEach(function (person) {
//   console.log(person);
// });

// people.forEach((person) => console.log(person));

// ======== Map
// const newPeople = people.map((person) => {
//   // return person;
//   // return 'Hello';
//   // return person.name;
//   return `${person.name}:${person.age}`;
// });
// console.log(newPeople);

// const newPeople = people.map(person => `${person.name}:${person.budget}`)
// const newPeople = people.map((person) => person.age * 3);
// console.log(newPeople);

// ======== Filter
// const moneyKeepers = [];
// for (let i = 0; i < people.length; i++) {
//   if (people[i].budget >= 50000) {
//     moneyKeepers.push(people[i]);
//   }
// }
// console.log(moneyKeepers);

// const adults = people.filter((person) => {
//   if (person.age >= 20) {
//     return true;
//   }
// });
// console.log(adults);

// const adults = people.filter((person) => person.age >= 30);
// console.log(adults);

// ======== Reduce
// let amount = 0;
// for (let i = 0; i < people.length; i++) {
//   amount += people[i].budget;
// }
// console.log(amount);

// const amount = people.reduce((total, person) => {
//   return total + person.budget;
// }, 0);
// console.log('amount after reduce:', amount);

// const amount = people.reduce((total, person) => total + person.budget, 0);
// console.log(amount + amount);

// ======== Find
// const agent = people.find(person => person.name === 'Smith');
// console.log(agent);

// ======== FindIndex
// const agentIndex = people.findIndex(person => person.name === 'Smith');
// console.log(agentIndex);

// ======== ======== ========

const amount = people
  .filter((person) => person.budget >= 20000)
  .map((person) => {
    return {
      info: `${person.name} (${person.age})`,
      budget: Math.sqrt(person.budget),
    };
  })
  .reduce((total, person) => total + person.budget, 0);

console.log(amount);
