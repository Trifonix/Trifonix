console.log("Start");

console.log("Start 2");

function timeout2sec() {
  console.log('timeout2sec');
}

window.setTimeout(function () {
  console.log("Inside Timeout");
}, 5000);

setTimeout(timeout2sec, 2000);

console.log("End");

// Event Loop

// latenflip.com
