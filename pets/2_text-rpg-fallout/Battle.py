from Hero import Hero
from Character import Character

class Battle:
    def __init__(self, hero: Hero, enemy: Character):
        self.hero = hero
        self.enemy = enemy

    def start(self):
        while self.hero.is_alive() and self.enemy.is_alive():
            print("\nСостояние боя:")
            print(self.hero)
            print(self.enemy)

            action = input("Выберите действие (атака/лечить/инвентарь): ").lower()

            if action == "атака":
                self.hero.attack(self.enemy)
            elif action == "лечить":
                if "Аптечка" in self.hero.inventory:
                    self.hero.heal(30)
                    self.hero.inventory.remove("Аптечка")
                else:
                    print("Аптечки нет!")
            elif action == "инвентарь":
                self.hero.show_inventory()
                continue
            else:
                print("Неверное действие!")
                continue

            if self.enemy.is_alive():
                self.enemy.attack(self.hero)
            else:
                print(f"{self.enemy.name} повержен!")
                break

        if not self.hero.is_alive():
            print("Вы погибли! Игра окончена.")
        else:
            print("Вы победили!")
