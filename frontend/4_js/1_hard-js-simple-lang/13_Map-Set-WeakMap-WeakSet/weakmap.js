let obj = { name: "Weakmap" };

// const arr = [objj];

// obj = null;

// console.log(obj);
// console.log(arr[0]);

const map = new WeakMap([[obj, "obj data"]]);
// get set delete has

obj = null;

// console.log(map.has(obj));
// console.log(map.get(obj));
// console.log(map);

// ======== ======== ========

const cache = new WeakMap();

function cacheUser(user) {
  if (!cache.has(user)) {
    cache.set(user, Date.now());
  }
  return cache.get(user);
}

let agent = { name: "Smith" };
let first = { name: "Neo" };

cacheUser(agent);
cacheUser(first);

agent = null

// console.log(cache.has(agent));
// console.log(cache.has(first));
// console.log(cache.get(first));
