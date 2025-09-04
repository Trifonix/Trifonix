// В js построено на "прототипах"

class Human {
    static isHuman = true

    humanGreet() {
        console.log("Greet from human!");
        // return 42
    }

    toString() {
        console.log('to string!!!');
    }
}

// Реализация Абстрации
class Person extends Human {
    constructor(name, age) {
        super()
        this.name = name ?? 'Undefined name'
        this.age = age ?? 'Undefined age'
    }

    sayHello() {
        console.log('Hello from = ', this.name);
    }
}

const newPerson1 = new Person('Neo', 28)
const newPerson2 = new Person('Smith', 33)

// newPerson1.sayHello()
// newPerson2.sayHello()

// Прототипированная цепочка
// console.log(newPerson1);
// console.log(newPerson1.humanGreet());

// console.log(newPerson1.toString());

// console.log(newPerson1.isHuman);

console.log(Human.isHuman);
console.log(Person.isHuman);
