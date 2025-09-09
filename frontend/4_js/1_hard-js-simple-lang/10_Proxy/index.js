// Wrapper
const withDefaultValue = (target, defaultValue = 0) => {
  return new Proxy(target, {
    get: (obj, prop) => (prop in obj ? obj[prop] : defaultValue),
  });
};

const position = withDefaultValue(
  {
    x: 24,
    y: 42,
  },
  0
);

// console.log(position);

// Hidden properties
const withHiddenProps = (target, prefix = "_") => {
  return new Proxy(target, {
    has: (obj, prop) => prop in obj && !prop.startsWith(prefix),
    ownKeys: (obj) => Reflect.ownKeys(obj).filter((p) => !p.startsWith(prefix)),
    get: (obj, prop, receiver) => (prop in receiver ? obj[prop] : void 0),
  });
};

const data = withHiddenProps({
  name: "Smith",
  age: 33,
  _uid: "123123123",
});

// Optimization
// const userData =

// const index = {};
// userData.forEach(i => index[i.id] = i);

const IndexedArray = new Proxy(Array, {
  construct(target, [args]) {
    const index = {};
    args.forEach((item) => (index[item.id] = item));

    return new Proxy(new target(...args), {
      get(arr, prop) {
        switch (prop) {
          case "push":
            return (item) => {
              index[item.id] = item;
              arr[prop].call(arr, item);
            };
          case "findById":
            return (id) => index[id];
          default:
            return arr[prop];
        }
      },
    });
  },
});

const users = new IndexedArray([
  { id: 1, name: "John", job: "Fullstack", age: 22 },
  { id: 2, name: "Johny", job: "Backend", age: 24 },
  { id: 3, name: "Johns", job: "Frontend", age: 26 },
  { id: 4, name: "Johnz", job: "Lead", age: 28 },
]);
