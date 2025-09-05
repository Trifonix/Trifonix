// const car = {
//   model: 'Tesla',
//   year: 2023
// }

// const json = JSON.stringify(car)
// const parsed = JSON.parse(json)

// console.log(json);
// console.log(parsed);

const list = document.querySelector("#list");
const filter = document.querySelector("#filter");
let USERS = [];

filter.addEventListener("input", (event) => {
  const value = event.target.value.toLowerCase();
  const filteredUsers = USERS.filter((user) =>
    user.name.toLowerCase().includes(value)
  );
  render(filteredUsers);
});

async function start() {
  list.innerHTML = toHTML("Loading...");
  try {
    const resp = await fetch("https://jsonplaceholder.typicode.com/users");
    const data = await resp.json();
    // console.log(resp);
    // console.log(data);
    setTimeout(() => {
      USERS = data;
    }, 2000);
    render(data);
  } catch (err) {
    list.style.color = "coral";
    list.innerHTML = err.message;
  }
}

function render(user = []) {
  if (user.length === 0) {
    list.style.color = "coral";
    list.innerHTML = "NOBODY";
  } else {
    const html = user.map(toHTML).join("");
    list.innerHTML = html;
  }
}

function toHTML(user) {
  if (user !== "Loading...") {
    return `
      <li class="list-group-item">${user.name}</li>
    `;
  } else return `<li class="list-group-item">${user}</li>`;
}

start();
