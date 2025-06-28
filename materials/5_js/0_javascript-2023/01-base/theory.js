// ======== More operators
let a = 1;
let b = 2;
let c = 0;

c = c + a;
c = c - a;
c = c * a;
c = c / a;

c += a;
c -= a;
c *= a;
c /= a;

// ======== Data Types
const age = 29;                   // number
const name = 'John';              // string
const isProg = true;              // boolean
let x;                            // undefined
// ?                              null
console.log(typeof x);            // undefined
console.log(typeof null);         // object
console.log(typeof function(){}); // function
console.log(1 / x);               // NaN
console.log(typeof (1 / x));      // number
console.log(typeof NaN);          // number

// ======== Priorities
const fullAge = 29;
const birthYear = 1990;
const currentYear = 2025;
// > < >= <=
const isFullAge = currentYear - birthYear >= fullAge;
console.log(isFullAge);           // true

const num01 = 42;
const num02 = '42';
console.log(num01 == num02);        // true
console.log(num01 === num02);       // false