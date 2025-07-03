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
  return name
});
console.log('newNames:', newNames);

console.log(newNames.includes('Bill'));
console.log(newNames.includes('Kiddo'));

console.log(newNames.indexOf('Kiddo') !== -1);
