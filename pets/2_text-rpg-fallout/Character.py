class Character:
    def __init__(self, name: str, hp: int, attack_power: int):
        self.name = name
        self._hp = hp                
        self.attack_power = attack_power

    def is_alive(self) -> bool:
        return self._hp > 0

    def take_damage(self, damage: int):
        self._hp = max(self._hp - damage, 0)
        print(f"{self.name} получил {damage} урона. Осталось {self._hp} HP.\n")

    def attack(self, other: "Character"):
        print(f"{self.name} атакует {other.name}!")
        other.take_damage(self.attack_power)

    def __str__(self):
        return f"{self.name} (HP: {self._hp}, Атака: {self.attack_power})"
