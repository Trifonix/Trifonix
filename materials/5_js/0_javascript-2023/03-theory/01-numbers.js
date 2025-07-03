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
