// const person = {
//   name: "Neo",
//   age: 28,
//   greet: function () {
//     console.log("Greet!");
//   },
// };

const person = new Object({
  name: "Smith",
  age: 33,
  greet: function () {
    console.log("Greet!");
  },
});

Object.prototype.sayHello = function () {
  console.log("Hello");
};

const trinity = Object.create(person);
trinity.name = "Trinity";

// const str = "I am string";

const str = new String("I am second string");
