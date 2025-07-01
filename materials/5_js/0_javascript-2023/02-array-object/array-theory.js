const names = ['Bill', 'Mamba', 'John', 'Garry'];

names.push('Dean');

console.log('Names: ', names);

names.unshift('Chuck');

console.log('Names: ', names);

names.shift();

console.log('Names: ', names);

const firstName = names.shift();

console.log(firstName);

const lastName = names.pop();

console.log(lastName);

console.log(names.reverse());

console.log(names.toReversed());

console.log(names.sort());

const letters = ['s', 'q', 'z', 'a', 'y', 'c'];
console.log(letters);

console.log(letters.sort());

console.log(letters.sort(function (a, b) {
  return b.charCodeAt(0) - a.charCodeAt(0);
}));

console.log(letters.toSorted());

console.log(names.splice(2, 1));

console.log(names);

console.log(names.toSpliced(1, 1));

console.log(names);

names.push('Mamba');

const greatWoman = 'Mamba';

const index = names.indexOf(greatWoman);

console.log(names);

console.log(index);
