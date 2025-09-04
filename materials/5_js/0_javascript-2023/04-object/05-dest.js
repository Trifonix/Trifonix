// Деструктуризация

const person = {
    // name: 'Smith',
    age: 40,
    isAgent: true,
    languages: ['en', 'binary'],
    address: {
      city: 'New-York',
      street: 'Avenue'
    }
}

// const name = person.name
// const age = person.age
// const languages = person.languages
// console.log(name, age, languages);

const name = 'Neo'

const {age, name: firstname = 'TEST', languages} = person
// console.log(languages)
// console.log(firstname);  
// console.log(age);

// Прототипное наследование
for (let key in person) {
    // console.log(key);
    if (person.hasOwnProperty(key)) {
        console.log(person[key]);
    }
}
// console.log([1, 2]);

