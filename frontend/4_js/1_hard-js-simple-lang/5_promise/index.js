console.log("Request data...");

// setTimeout(() => {
//   console.log("Preparing data...");

//   const backendData = {
//     server: "aws",
//     port: 80,
//     status: "working",
//   };

//   setTimeout(() => {
//     backendData.modified = true;
//     console.log("Data received:", backendData);
//   }, 2000);
// }, 2000);

// const p = new Promise(function (resolve, reject) {
//   setTimeout(() => {
//     console.log("Preparing data...");
//     const backendData = {
//       server: "aws",
//       port: 80,
//       status: "pWorking",
//     };
//     resolve(backendData);
//   }, 2000);
// });

// p.then((data) => {
//   const p2 = new Promise((resolve, reject) => {
//     setTimeout(() => {
//       data.modified = true;
//       resolve(data);
//     }, 2000);
//   });

//   p2.then((clientData) => {
//     console.log("Data received: ", clientData);
//   });
// });

// p.then((data) => {
//   return new Promise((resolve, reject) => {
//     setTimeout(() => {
//       data.modified = true;
//       // resolve(data);
//       reject(data);
//     }, 2000);
//   });
// })
//   .then((clientData) => {
//     clientData.fromPromise = true;
//     return clientData;
//   })
//   .then((data) => {
//     console.log("Modified data", data);
//   })
//   .catch((err) => console.error("Error:", err))
//   .finally(() => console.log("Finally"));

// const sleep = (ms) => new Promise((resolve) => setTimeout(() => resolve(), ms));

const sleep = (ms) => {
  return new Promise((resolve) => {
    setTimeout(() => resolve(), ms);
  });
};

// sleep(2000).then(() => console.log("After 2 sec"));
// sleep(3000).then(() => console.log("After 3 sec"));

Promise.all([sleep(2000), sleep(4200)]).then(() => {
  console.log("All promises");
});

Promise.race([sleep(2000), sleep(4200)]).then(() => {
  console.log("Race promises");
});
