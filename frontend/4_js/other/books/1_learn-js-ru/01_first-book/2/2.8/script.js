// 1
let a = 1, b = 1;
let c = ++a; // 2
let d = b++; // 1
console.log('\nзадача 1:');
console.log(c, d, '\n');


// 2
let aa = 2;
let x = 1 + (aa *= 2); // 5
console.log('задача 2:');
console.log(x);

// 3
console.log('\nзадача 3:');
console.log("" + 1 + 0); // 10
console.log("" - 1 + 0); // -1
console.log(true + false); // 1
console.log(6 / "3"); // 2
console.log("2" * "3"); // 6
console.log(4 + 5 + "px"); // 9px
console.log("$" + 4 + 5); // $45
console.log("4" - 2); // 2
console.log("4px" - 2); // NaN
console.log("  -9  " + 5); //   -9  5
console.log("  -9  " - 5); // -14
console.log(typeof (+null), null + 1); // 1
console.log(undefined + 1); // NaN
console.log(typeof (-" \t \n"), " \t \n" - 2); //  -2

// 4
console.log('\nзадача 4:');
let aaa = +prompt("Первое число?", 1);
let bbb = +prompt("Второе число?", 2);
alert(aaa + bbb); // 3
