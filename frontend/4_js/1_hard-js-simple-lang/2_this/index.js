function hello() {
  console.log("Hello, World!", this);
}

const person = {
  name: "John",
  age: 29,
  sayHello: hello,
  // sayHelloWindow: hello.bind(window),
  // sayHelloWindow: hello.bind(this),
  sayHelloWindow: hello.bind(document),
  logInfo: function (job, phone) {
    console.group(`${this.name} info:`);
    console.log(`Name is ${this.name}`);
    console.log(`Age is ${this.age}`);
    console.log(`Job is ${job}`);
    console.log(`Phone is ${phone}`);
    console.groupEnd();
  },
};

const agent = {
  name: "Smith",
  age: 32,
};

// const fnAgentInfoLog = person.logInfo.bind(agent);
// fnAgentInfoLog("Frontend", "8-999-123-45-67");

// const fnAgentInfoLog = person.logInfo.bind(agent, "Frontend", "8-676-123-45-67");
// fnAgentInfoLog();

// person.logInfo.bind(agent, "Frontend", "8-888-123-45-67")();
// person.logInfo.call(agent, "FrontendCall", "7-555-123-45-67");
person.logInfo.apply(agent, ["FrontendApply", "8-888-123-45-67"]);

/// ============

const array = [1, 2, 3, 4, 5];

// function multBy(arr, n) {
//   return arr.map(function (i) {
//     return i * n;
//   });
// }

Array.prototype.multBy = function (n) {
  // console.log("multBy", this);
  return this.map(function (i) {
    return i * n;
  });
};

array.multBy(2);

console.log(array.multBy(20));

// console.log(multBy(array, 4));
