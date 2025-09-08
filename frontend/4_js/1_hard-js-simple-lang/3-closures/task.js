/**
 * Написать свою функцию bind
 * Пример работы:
 *
 * function logPerson() {
 *     console.log(`Person: ${this.name}, ${this.age}, ${this.job}`);
 * }
 *
 * const person1 = {name: 'Neo', age: 28, job: 'Dev'};
 * const person2 = {name: 'Smith', age: 33, job: 'Agent'};
 *
 * bind(person1, logPerson)
 * bind(person2, logPerson)
 */

function bind(context, fn) {
  return function (...args) {
    fn.apply(context, args);
  };
}

function logPerson() {
  console.log(`Person: ${this.name}, ${this.age}, ${this.job}`);
}

const person1 = { name: "Neo", age: 28, job: "Dev" };
const person2 = { name: "Smith", age: 33, job: "Agent" };

bind(person1, logPerson)();
bind(person2, logPerson)();
