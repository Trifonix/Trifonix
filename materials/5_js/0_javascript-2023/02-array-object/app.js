// Theory
/*
const array = [1, 2, 3, 5, 20];
console.log(array);

const arrayString = ['a', 'b', 'c'];
console.log(arrayString);

const newArray = new Array(1, 2, 3, 5, 10);
console.log(newArray);
console.log(newArray.length);
console.log(newArray[1]);
console.log(newArray[newArray.length - 1]);

array[0] = 'hi';
console.log(array);

array[array.length] = 'becon'; // bad practice
console.log(array);
*/

// Practice
const inputElement = document.getElementById("title");
const createBtn = document.getElementById("create");
const listElement = document.getElementById("list");

console.log(inputElement.value);

// const notes = ["note 1", "note 2"];
/*
function render() {
  // for (let i = 0; i < notes.length; i++) {
  //   listElement.insertAdjacentHTML("beforeend", getNoteTemplate(notes[i]));
  // }
  for (let note of notes) {
    listElement.insertAdjacentHTML("beforeend", getNoteTemplate(note));
  }
}
render();
*/
// createBtn.onclick = function () {
//   if (inputElement.value.length === 0) {
//     return;
//   }
//   listElement.insertAdjacentHTML(
//     "beforeend",
//     getNoteTemplate(inputElement.value)
//   );
//   inputElement.value = "";
// };

// function getNoteTemplate(title) {
//   return `
//     <li
//       class="list-group-item d-flex justify-content-between align-items-center"
//     >
//       <span>${title}</span>
//       <span>
//         <span class="btn btn-small btn-success">&check;</span>
//         <span class="btn btn-small btn-danger">&times;</span>
//       </span>
//     </li>
//   `;
// }

/**
 * Object Theory
 
const person = {
  firstName: "John",
  secondName: "Smith",
  year: 1990,
  hasPartner: true,
  languages: ['ru', 'en', 'es'],
  getFullName: function() {
    console.log(person.firstName + ' ' + person.secondName)
  }
};
console.log(typeof person);
person.getFullName();

console.log(person.firstName);
console.log(person['secondName']);
const key = 'hasPartner';
console.log(person[key]);
person.hasPartner = false;
console.log(person.hasPartner);
*/

const notes = [
  {
    title: "записать блок про массивы",
    completed: false,
  },
  {
    title: "рассказать теорию объектов",
    completed: true,
  },
];

function render() {
  // for (let note of notes) {
  //   listElement.insertAdjacentHTML("beforeend", getNoteTemplate(note));
  // }
  listElement.innerHTML = "";
  if (notes.length === 0) {
    listElement.innerHTML = '<p>Список пуст...</p>';
  }
  for (let i = 0; i < notes.length; i++) {
    listElement.insertAdjacentHTML("beforeend", getNoteTemplate(notes[i], i));
  }
}
render();

createBtn.onclick = function () {
  if (inputElement.value.length === 0) {
    return;
  }
  const newNote = {
    title: inputElement.value,
    completed: false,
  };
  // listElement.insertAdjacentHTML(
  //   "beforeend",
  //   getNoteTemplate(newNote)
  // );
  notes.push(newNote);
  render();
  inputElement.value = "";
};

listElement.onclick = function (event) {
  if (event.target.dataset.index) {
    // const index = Number(event.target.dataset.index);
    const index = parseInt(event.target.dataset.index);
    const type = event.target.dataset.type;

    if (type === 'toggle') {
      notes[index].completed = !notes[index].completed;
    } else if (type === 'remove') {
      notes.splice(index, 1);
    }

    render();
  }
};

function getNoteTemplate(note, index) {
  return `
    <li
      class="list-group-item d-flex justify-content-between align-items-center"
    >
      <span class="${note.completed ? "text-decoration-line-through" : ""}">${
    note.title
  }</span>
      <span>
        <span class="btn btn-small btn-${
          note.completed ? "warning" : "success"
        }" data-index=${index} data-type="toggle">&check;</span>
        <span class="btn btn-small btn-danger" data-index=${index} data-type="remove">&times;</span>
      </span>
    </li>
  `;
}

const a = { a: 1 };
console.log(a.toString()); // [object Object]
