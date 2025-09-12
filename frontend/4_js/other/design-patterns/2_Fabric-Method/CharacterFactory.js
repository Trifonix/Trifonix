export class CharacterFactory {
  static createCharacter(type, name) {
    switch (type.toLowerCase()) {
      case "wizard":
        return new Wizard(name);
      case "warrior":
        return new Warrior(name);
      case "archer":
        return new Archer(name);
      default:
        throw new Error(`Неизвестный тип персонажа: ${type}`);
    }
  }
}
