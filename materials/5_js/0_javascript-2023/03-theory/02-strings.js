const myName = "Neo";
const age = "29";

const output = `any
qwe
string`;
console.log(output);

const old = "Hello, I am " + myName + "   and my age is " + age;
console.log(old);

const newStr = `My name is ${myName}`;
console.log(newStr);

function getAge() {
  return age;
}
console.log(`it will be result of func: ${getAge()}`);

console.log(`you can or not ? ${getAge() > 18 ? "yes" : "not"}`);

console.log(`can\'t breathe`);

console.log(myName);
console.log(myName.length);
console.log(myName.toUpperCase);
console.log(myName.toLowerCase);
console.log(myName.charAt(0));
console.log(myName.indexOf('e'));
console.log(myName.startsWith('Ne'));
console.log(myName.toLowerCase().startsWith('ne'));
