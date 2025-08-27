from Character import Character

player = Character(name="Игрок", hp=100, attack_power=20)
enemy = Character(name="Гоблин", hp=50, attack_power=10)

print(player)
print(enemy)

player.attack(enemy)
enemy.attack(player)
