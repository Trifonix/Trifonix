import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.intellect = 50
        self.inventory = ["Death Note"]
    
    def attack_enemy(self):
        return random.randint(1, 10)
    
    def death_note_attack(self):
        if "Death Note" in self.inventory:
            return 999
        return self.attack_enemy()
