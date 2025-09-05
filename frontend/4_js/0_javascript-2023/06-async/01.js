// Event Loop

// const to = setTimeout(() => {
//   console.log("after 2 sec");
// }, 2000);

// clearTimeout(to);

// setTimeout(() => {
//   console.log("after 3 sec");
// }, 3000);

// let count = 0;
// setInterval(() => {
//   console.log("tick", count++);
// });

// function delay(callback, time = 1000) {
//   setTimeout(callback, time);
// }

// delay(() => {
//   console.log("timeout");
// }, 2000);

// promise (промисы)

const delay = (time = 1000) => {
  const promise = new Promise((resolve, reject) => {
    setTimeout(() => {
      // resolve([1, 2, 3]);
      reject("Error in delay");
    }, time);
  });
  return promise;
};

// delay(2500)
//   .then((data) => {
//     console.log("Timeout", data);
//     return data.map((x) => x * x);
//   })
//   .then((data) => {
//     console.log(data);
//   })
//   .catch((err) => {
//     console.log(err);
//   })
//   .finally(() => console.log("Finally"));

// chaining (чейнинг)

const getData = () => new Promise(resolve => resolve([1, 2, 3, 4, 5]))

// getData().then(array => console.log(array));

// async, await (синтаксис с си-шарпа)

async function asyncExample() {
  try {
    await delay(3000)
    const data = await getData();
    console.log(data);
  } catch (err) {
    console.log(err);
  } finally {
    console.log("Finally");
  }
}
asyncExample();
