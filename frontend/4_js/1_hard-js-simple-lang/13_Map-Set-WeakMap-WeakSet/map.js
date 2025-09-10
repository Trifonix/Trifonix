const obj = {
  name: "Neo",
  age: 29,
  job: "swe",
};

const entries = [
  ["name", "Neo"],
  ["age", 29],
  ["job", "swe"],
];

// console.log(Object.entries(obj));
// console.log(Object.fromEntries(entries));

const map = new Map(entries);
// console.log(map);
// console.log(map.get('job'));
// console.log(obj.job);

map.set("newField", 42).set(obj, "Value of object").set(NaN, "NaN ??");
// console.log(map);

// console.log(map.get(obj));
// console.log(map.get(NaN));

// map.delete("job");
// console.log(map.has("job"));

// console.log(map.size);
// map.clear();
// console.log(map.size);

// ======== ======== ========

// for (let [key, value] of map.entries()) {
//   console.log(key, value);
// }

// for (let val of map.values()) {
//   console.log(val);
// }

// for (let key of map.keys()) {
//   console.log(key);
// }

// map.forEach((val, key, m) => {
//   console.log(val, key);
// });

// ======== ======== ========

// const arr = [...map];
const arr = Array.from(map);

const mapObj = Object.fromEntries(map.entries());

// console.log(arr);
// console.log(mapObj);

// ======== ======== ========

const users = [{ name: "John" }, { name: "Vick" }, { name: "Dean" }];

const visits = new Map();

visits
  .set(users[0], new Date())
  .set(users[1], new Date(new Date().getTime() + 1000 * 60))
  .set(users[2], new Date(new Date().getTime() + 5000 * 60));

function lastVisit(user) {
  return visits.get(user);
}

// console.log(lastVisit(users[2]));
