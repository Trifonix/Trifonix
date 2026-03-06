const firstName = "Neo";
const lastName = "Matrix";
const age = 28;
const str = "Hello, my name is Neo";

let value;

value = firstName + lastName;
value = firstName + ' ' + lastName;
value = value + " I am " + age;
value += " I am " + age;

value = firstName.length;
value = firstName[2];
value = lastName[lastName.length-1];

value = firstName.toUpperCase();
value = lastName.concat(' ', firstName);
value = lastName.indexOf('x');
value = lastName.indexOf('!');
value = str.includes('my');

value = str.slice(0, 3);
value = str.replace('my', 'his');

document.body.innerHTML = `<h1>${value}</h1>`;
