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
        // console.log(person[key]);
    }
}
// console.log([1, 2]);

// console.dir(Object);

// Object.keys(person).forEach((key) => {
//     console.log(person[key] + '!!');
// })

const logger = {

    keys(withText = true) {
        if (withText) {
            console.log('Object keys: ', Object.keys(this));
        } else {
            console.log(Object.keys(this));
        }
    },

    keysAndValues() {
        Object.keys(this).forEach((key) => {
            console.log('Key: ', key);
            console.log('Value: ', this[key]);
        })
    }
}

// logger.keys()
// logger.keysAndValues()
// logger.keys(person)

const bound = logger.keys.bind(person)
bound(false)

// logger.keys.bind(person)()

logger.keys.call(person, false)

logger.keys.apply(person, [true])
