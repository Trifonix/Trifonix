let num = 42;
let firstName = "John";
num = 10;
const isProgrammer = true;
// firstName = "Dean";
// isProgrammer = false;
// ошибка, там константа
/* 
Многострочный 
комментарий 
*/
/* Can do
let $ = "test";
let $num = 8;
let num$ = 4;
let _ = 49;
let _num = 12;
let num_ = 14;
let first_name = "Alisa"; // snake_case
let javaScriptStyle = "Good!"; // camelCase
let PascalStyle = "normal"; // PascalCase
let num42 = 10;
*/
/* Restricted (запрещенные)
let 42num = 0;
let my-num = 0;
let false = '';
*/
//alert(num);
console.log(num);
console.log("Test:", firstName);
console.log(num + 10);
//number
//string
//boolean
// - * / минус умножить делить
// 4.2 float
let num2 = num + 2;
console.log(num, num2);
num = num2 - num;
console.log(num, num2);
let num3 = (num + num2) * 2;
console.log(num3);
const fullName = firstName + " " + "Doo";
console.log(fullName);

// Начинаем разрабатывать калькулятор

const resultElement = document.getElementById("result");
console.log(resultElement);
console.log(resultElement.textContent);
resultElement.textContent = 18;
// const input1 = document.getElementById("input1");
// const input2 = document.getElementById("input2");
// console.log(input1.value);
// console.log(input2.value);
// console.log(typeof input1.value);
// resultElement.textContent = Number(input1.value) + +input2.value;

const submitBtn = document.getElementById("submit");
submitBtn.onclick = function () {
  // console.log("Hello, click!");
  const input1 = document.getElementById("input1");
  const input2 = document.getElementById("input2");
  resultElement.textContent = Number(input1.value) + +input2.value;
};
