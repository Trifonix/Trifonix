// Числа
// Хотим переприсваивать значение
const a = 42;
const b = 2;
let c;
c = a + b;
console.log(c+c);

value = 0.6 + 0.7;
console.log(value); // 1.2999999999999998
// Способ получить 1.3 (#1)
value1 = ( 0.6 * 10 + 0.7 * 10 ) / 10;
console.log(value1);
// Способ получить 1.3 (#2)
value2 = parseFloat(value.toFixed(1));
console.log(value2);
console.log("====$====$====$====$");

// Math
valueMath = Math.PI; // 3.141592653589793
valueMath = Math.random(); // 0.08282516208182
valueMath = Math.round(2.4); // 2
valueMath = Math.ceil(2.1); // 3
valueMath = Math.floor(2.9); // 2
valueMath = Math.min(2, 12, 15, 0, 12); // 0
valueMath = Math.floor(Math.random() * 10 + 1) // 10
console.log(valueMath);

// Array
const arr = ['black', 'red', 'yellow', 'green'];
valueArr = Math.floor(Math.random() * arr.length);
console.log(valueArr, arr[valueArr]); // 2 'yellow'
