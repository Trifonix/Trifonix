let a = '1';
let value = 5;

if (a > 0) {
  value = a;
} else {
  value += 1;
}

// выражение ? если true : если false;

value = a === 1 ? 8 : 42;

let color = 'orange';

switch(color) {
  case 'yellow':
    value = 1;
    break;
  case 'red':
    value = 2;
    break;
  case 'orange':
    value = 100;
    break;
  default:
    value = 0;
}

document.body.innerHTML = value;
