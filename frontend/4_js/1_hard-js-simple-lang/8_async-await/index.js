const delay = (ms) => {
  return new Promise((r) => setTimeout(() => r(), ms));
};

delay(2000).then(() => console.log("2 sec"));

const url = "https://jsonplaceholder.typicode.com/todos";

// function fetchTodos() {
//   console.log("Fetch Todo start");
//   return delay(2500)
//     .then(() => fetch(url))
//     .then((response) => response.json());
// }

// fetchTodos()
//   .then((data) => {
//     console.log("Data:", data);
//   })
//   .catch((e) => console.error(e));

async function fetchAsyncTodos() {
  console.log("Fetch Todo start");
  try {
    await delay(3000);
    const response = await fetch(url);
    const data = await response.json();
    console.log("Data:", data);
  } catch (e) {
    console.error(e);
  } finally {
    console.log("Finally from try-catch");
  }
}

fetchAsyncTodos();
