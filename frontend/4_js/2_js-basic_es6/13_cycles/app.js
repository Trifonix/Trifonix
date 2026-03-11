// while, do while, for, for of, for in

let value = '';
let i = 10;

while(i--) {
  value += i + ' ';
}

document.body.innerHTML = value;
value += '<hr>';

let x = 0;
do {
  value += x + ' ';
  x++;
} while (x < 10);

document.body.innerHTML = value;
value += '<hr>';

let str = 'hello';

for (let y = 0; y < str.length; y++) {
  value += str[y] + '*';
}

document.body.innerHTML = value;
value += '<hr>';

let myObj = {
  name: 'Neo',
  age: 28
}

for (let key in myObj) {
  value += key + '<br>';
  value += myObj[key] + '<br><br>';
}

value += '<hr>';
document.body.innerHTML = value;

