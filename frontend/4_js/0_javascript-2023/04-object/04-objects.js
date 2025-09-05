// console.log('test');

const person = {
  name: 'Smith',
  age: 40,
  isAgent: true,
  languages: ['en', 'binary'],
  address: {
    city: 'New-York',
    street: 'Avenue'
  },
  'complex key': 'complex value',
  [1 + 2]: 'computed value',
  [new Date().getTime()]: 'computed value',
  ['key_' + 21 * 2]: 'computed value',
  greet() {
    console.log('Greet from person', this);
  },
  arrow: () => {
    console.log('Person Arrow', this);
  },
  info() {
    console.log(this);
    console.log('Person name:', this.name);
  }
};
/*
console.log(typeof person);
console.log(typeof null); // object ? косяк javascript ?
*/
console.log(person);
person.greet();
person.arrow();
person.info();

person.greet();

// window === this --- True

console.log(person.address);
console.log(person['address']);
console.log(person['complex key']);
const addressKey = 'address';
console.log(person[addressKey]);

person.age++;
console.log(person.age);

person.languages.push('de');
console.log(person.languages);

person.address = undefined;
console.log(person.address);

delete person.address;
console.log((person.address));
console.log(person);