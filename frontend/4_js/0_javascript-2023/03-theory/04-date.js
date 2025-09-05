// console.log(new Date());

const now = new Date();

// const start = new Date();
// const start = new Date(0);
// const start = new Date(1000 * 60 * 60 * 24 * 365);

const date = new Date(2011, 0, 1, 12, 42, 21);

console.log(date);

console.log(now.getFullYear());

console.log(now.getMonth());

console.log(now.getDate());

console.log(now.getHours());

console.log(now.getMinutes());

console.log(now.getSeconds());

console.log(now.getMilliseconds());

now.setFullYear(2055);

console.log(now);

console.log(now.toDateString());

console.log(now.toTimeString());

console.log(now.toLocaleDateString());

console.log(now.toLocaleTimeString());

// ========

let mode = "full";
const output = document.getElementById("output");
const fullBtn = document.getElementById("full");
const dateBtn = document.getElementById("date");
const timeBtn = document.getElementById("time");

function bindMode(name) {
  return function () {
    mode = name;
    update();
  };
}

fullBtn.onclick = bindMode("full");
dateBtn.onclick = bindMode("date");
timeBtn.onclick = bindMode("time");

setInterval(update, 100);
update();
function update() {
  output.textContent = format(mode);
}

// Pure Function
function format(formatMode) {
  const now = new Date();
  switch (formatMode) {
    case "time":
      return now.toLocaleTimeString() + '.' + now.getMilliseconds();
    case "date":
      return now.toLocaleDateString();
    case "full":
      return now.toLocaleDateString() + " " + now.toLocaleTimeString();
    default:
      return now.toLocaleTimeString();
  }
}
