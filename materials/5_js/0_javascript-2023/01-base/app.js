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
// console.log(num);
// console.log("Test:", firstName);
// console.log(num + 10);
//number
//string
//boolean
// - * / минус умножить делить
// 4.2 float
let num2 = num + 2;
// console.log(num, num2);
num = num2 - num;
// console.log(num, num2);
let num3 = (num + num2) * 2;
// console.log(num3);
const fullName = firstName + " " + "Doo";
// console.log(fullName);

// Начинаем разрабатывать калькулятор

const resultElement = document.getElementById("result");
// console.log(resultElement);
// console.log(resultElement.textContent);
resultElement.textContent = 18;
// const input1 = document.getElementById("input1");
// const input2 = document.getElementById("input2");
// console.log(input1.value);
// console.log(input2.value);
// console.log(typeof input1.value);
// resultElement.textContent = Number(input1.value) + +input2.value;

const submitBtn = document.getElementById("submit");
// submitBtn.onclick = function () {
//   console.log("Hello, click!");
//   const input1 = document.getElementById("input1");
//   const input2 = document.getElementById("input2");
//   resultElement.textContent = Number(input1.value) + +input2.value;
// };

const plusBtn = document.getElementById("plus");
const minusBtn = document.getElementById("minus");
let action = '+';

plusBtn.onclick = function () {
  action = '+';
};

minusBtn.onclick = function () {
  action = '-';
};

function printResult(result) {
  console.log('Result to print', result);
  if (result < 0) {
    resultElement.style.color = 'red';
  } else {
    resultElement.style.color = 'green';
  }
  resultElement.textContent = result;
}

function computeNumbersWithAction(input1, input2, actionSymbol) {
  // const value1 = +input1.value;
  // const value2 = +input2.value;
  const value1 = +input1.value;
  const value2 = +input2.value;
  // if (actionSymbol == '+') {
  //   return value1 + value2;
  // } else if (actionSymbol == '-') {
  //   return value1 - value2;
  // }

  // return (actionSymbol == '+') ? value1 + value2 : value1 - value2;

  // console.log(value1, value2);
  // console.log(typeof value1, typeof value2);

  // debugger

  const result = actionSymbol == '+' ? value1 + value2 : value1 - value2;
  // console.log(result);
  return result;
}

submitBtn.onclick = function () {
  // let res = '';
  // if (action == '+') {
  //   res = Number(input1.value) + +input2.value;
  //   printResult(res);
  // } else if (action == '-') {
  //   res = Number(input1.value) - +input2.value;
  //   printResult(res);
  // }
  const result = computeNumbersWithAction(input1, input2, action);
  printResult(result);
};
