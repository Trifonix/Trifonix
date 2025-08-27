import random

class Enemy:
    def __init__(self, name, hp, attack_range=(1,5)):
        self.name = name
        self.hp = hp
        self.attack_range = attack_range
    
    def attack_player(self):
        return random.randint(*self.attack_range)
