const person = Object.create(
  {
    calculateAge() {
      console.log("Age", new Date().getFullYear() - this.birthYear);
    },
  },
  {
    name: {
      value: "Neo",
      enumerable: true,
      configurable: true,
    },
    birthYear: {
      value: 1971,
      enumerable: false,
      writable: true,
    },
    age: {
      get() {
        return new Date().getFullYear() - this.birthYear;
      },
      set(value) {
        document.body.style.background = "salmon";
        console.log("Set age", value);
      },
    },
  }
);

// console.log(person);

// const person = {
//   name: 'Smith',
//   birthYear: 1970
// }

// person.name = "Smith";
// person.birthYear = 1966;

// delete person.name;
// delete person.birthYear;

for (let key in person) {
  if (person.hasOwnProperty(key)) {
    console.log("Key", key, person[key]);
  }
}
console.log(person.birthYear);
console.log(person.age);
