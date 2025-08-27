from Character import Character

class Hero(Character):
    def __init__(self, name: str, hp: int, attack_power: int):
        super().__init__(name, hp, attack_power)
        self.inventory = []

    def add_item(self, item: str):
        self.inventory.append(item)
        print(f"{item} добавлен в инвентарь {self.name}.")

    def show_inventory(self):
        if not self.inventory:
            print(f"Инвентарь {self.name} пуст.")
        else:
            print(f"Инвентарь {self.name}: {', '.join(self.inventory)}")

    def heal(self, amount: int):
        self._hp += amount
        print(f"{self.name} восстановил {amount} HP. Сейчас HP: {self._hp}")
