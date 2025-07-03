const names = ["Bill", "Mamba", "John", "Garry"];

names.push("Dean");

console.log("Names: ", names);

names.unshift("Chuck");

console.log("Names: ", names);

names.shift();

console.log("Names: ", names);

const firstName = names.shift();

console.log(firstName);

const lastName = names.pop();

console.log(lastName);

console.log(names.reverse());

console.log(names.toReversed());

console.log(names.sort());

const letters = ["s", "q", "z", "a", "y", "c"];
console.log(letters);

console.log(letters.sort());

console.log(
  letters.sort(function (a, b) {
    return b.charCodeAt(0) - a.charCodeAt(0);
  })
);

console.log(letters.toSorted());

console.log(names.splice(2, 1));

console.log(names);

console.log(names.toSpliced(1, 1));

console.log(names);

names.push("Mamba");

const greatWoman = "Mamba";

const index = names.indexOf(greatWoman);

console.log(names);

console.log(index);

console.log("Momba was ?", names.indexOf("Momba"));

names[index] = "Beatriss";

console.log(names);

names.with(index, "Sambur");

console.log(names.with(index, "Sambur"));

console.log(names);

const arrLetters = letters.map(function (letter) {
  return letter.toUpperCase();
});

console.log(arrLetters);

console.log("actual names:", names);

const newNames = names.map(function (name, index) {
  if (index === 1) {
    return "Kiddo";
  }
  return name;
});
console.log("newNames:", newNames);

console.log(newNames.includes("Bill"));
console.log(newNames.includes("Kiddo"));

console.log(newNames.indexOf("Kiddo") !== -1);

const people = [
  { name: "user", money: 4200 },
  { name: "user1", money: 6200 },
  { name: "user2", money: 8400 },
  { name: "user3", money: 5000 },
];

console.log(people.indexOf({ budget: 5000 }));
console.log(people.indexOf({ name: "user3", money: 5000 }));

let findedPerson;

for (person of people) {
  if (person.money === 5000) {
    findedPerson = person;
  }
}
console.log(findedPerson);

const ourPerson = people.find(function (person) {
  if (person.money == 6200) {
    return true;
  }
});
console.log(ourPerson);

const ourPerson2 = people.find(function (person) {
  return person.name === "user";
});
console.log(ourPerson2);

const finded = people.find((p) => p.money === 6200);
console.log(finded);

const finded2 = people.findIndex(function (person) {
  return person.money === 5000;
});
console.log(finded2);
console.log(people[finded2]);

console.log(people.with(finded2, 42));

let sumMoney = 0;
const filtered = people.filter(function (p) {
  return p.money > 5500;
});
console.log(filtered);

filtered.forEach(function (p) {
  sumMoney += p.money;
});
console.log(sumMoney);

const sumMoney2 = people
  .filter((p) => p.money > 5500)
  .map((p) => p.money)
  .reduce((acc, p) => acc + p, 0);
console.log(sumMoney2);

const byMoney = (p) => p.money > 5500;
const pickMoney = (p) => p.money;

const sumMoney3 = people
  .filter(byMoney)
  .map(pickMoney)
  .reduce((acc, p) => acc + p, 0);
console.log(sumMoney3);

const string = "Привет, как дела?";
const reversed = string.split();
console.log(reversed);

const reversed2 = string.split(',');
console.log(reversed2);

const reversed3 = string.split('');
console.log(reversed3);

const reversed4 = string.split('').toReversed();
console.log(reversed4);

const reversed5 = string.split('').toReversed().join();
console.log(reversed5);

const reversed6 = string.split('').toReversed().join('');
console.log(reversed6);

const reversed7 = string.split('').toReversed().join('!');
console.log(reversed7);

const reversed8 = string.split('').toReversed().join('!').split('').filter(c => c !== '!').join('');
console.log(reversed8);

// [].
