import { CharacterFactory } from "./CharacterFactory.js";

class Character {
  constructor(name) {
    this.name = name;
    this.type = "character";
  }
}

class Wizard extends Character {
  constructor(name) {
    super(name);
    this.type = "wizard";
    this.spell = "fireball";
  }
}

class Warrior extends Character {
  constructor(name) {
    super(name);
    this.type = "warrior";
    this.weapon = "sword";
  }
}

class Archer extends Character {
  constructor(name) {
    super(name);
    this.type = "archer";
    this.bow = "longbow";
  }
}

// Используем фабрику для создания разных персонажей
const gandalf = CharacterFactory.createCharacter("wizard", "Гэндальф");
const aragorn = CharacterFactory.createCharacter("warrior", "Арагорн");
const legolas = CharacterFactory.createCharacter("archer", "Леголас");

console.log(gandalf); // Wizard { name: 'Гэндальф', type: 'wizard', spell: 'fireball' }
console.log(aragorn); // Warrior { name: 'Арагорн', type: 'warrior', weapon: 'sword' }
console.log(legolas); // Archer { name: 'Леголас', type: 'archer', bow: 'longbow' }

// Попытка создать неизвестного персонажа
try {
  CharacterFactory.createCharacter("knight", "Рыцарь");
} catch (error) {
  console.error(error.message); // "Неизвестный тип персонажа: knight"
}
