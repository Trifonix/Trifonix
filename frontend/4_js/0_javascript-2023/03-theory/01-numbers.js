const num = 42;       // integer
const float = 42.42;  // float
const pow = 10e3;     // pow
console.log(pow);

const big = 1000000;
console.log(big);

const bigNew = 1_000_000_000;
console.log(bigNew);

console.log(Number);
console.log(Number('42'));

console.dir(Number);
console.log(Number.MAX_SAFE_INTEGER);

console.log(Math);
console.log(Math.pow(2, 53) - 1);

console.log(Number.MIN_SAFE_INTEGER);

console.log(Number.MAX_VALUE);
console.log(Number.MIN_VALUE);

console.log(Number.POSITIVE_INFINITY);
console.log(Number.NEGATIVE_INFINITY);
console.log(1 / 0);

console.log(Number.isFinite(1 / 0));
console.log(Number.isFinite(Infinity));

console.log(23 / undefined);

const weird = 23 / undefined;
console.log(Number.isNaN(weird));
console.log(Number.isNaN(12));

const strInt = '42';
const strFloat = '42.42';
console.log(Number(strInt));
console.log(Number(strFloat));

console.log(Number.parseInt(strInt));
console.log(parseInt(strInt));

console.log(parseInt(strFloat));
console.log(parseFloat(strFloat));

console.log(+strInt, +strFloat);

console.log(0.1 + 0.2);
console.log((0.1 + 0.2).toFixed(1));
console.log((0.1 + 0.2).toFixed(10));
console.log(+((0.1 + 0.2).toFixed(10)));
console.log(parseFloat((0.1 + 0.2).toFixed(10)));

const fixed = (0.1 + 0.2).toFixed(10);
console.log(parseFloat(fixed));

// BigInt
console.log(Number.MAX_SAFE_INTEGER);
console.log(Number.MAX_SAFE_INTEGER + 1246987);
//console.log(BigInt(Number.MAX_SAFE_INTEGER) + 1246987);
console.log(BigInt(Number.MAX_SAFE_INTEGER) + 1246987n);

console.log(-42n);
console.log(typeof -42n);
// console.log(42.42n); error
// console.log(10n - 4);
console.log(parseInt(10n) - 4);
console.log(10n - BigInt(4));
console.log(5n / 2n);
console.log(5 / 2);

// Math
console.log(Math.E);
console.log(Math.PI);

console.log(Math.sqrt(25));
console.log(Math.pow(2, 3));
console.log(Math.abs(-42));
console.log(Math.max(2, 5, 42, 199, 0));
console.log(Math.min(2, 5, 42, 199, 0));
console.log(Math.floor(4.9));
console.log(Math.ceil(4.9));
console.log(Math.round(4.4));
console.log(Math.trunc(4.5));

console.log(Math.random());

function getRandomNumber(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
console.log(getRandomNumber(10, 100));
