class GameStats {
  static #instance = null;

  constructor() {
    if (GameStats.#instance) {
      throw new Error("Нельзя создать более одного экземпляра GameStats.");
    }
    this.stats = 0;
  }

  static getInstance() {
    if (!GameStats.#instance) {
      GameStats.#instance = new GameStats();
    }
    return GameStats.#instance;
  }
}

const stats1 = GameStats.getInstance();
const stats2 = GameStats.getInstance();
const stats3 = new GameStats();

console.log(stats1 === stats2);
console.log(stats1.stats);

stats1.stats = 10;
console.log(stats2.stats);
console.log(stats1.stats);
