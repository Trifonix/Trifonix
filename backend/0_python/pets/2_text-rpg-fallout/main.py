from Hero import Hero
from Character import Character
from Battle import Battle

player = Hero(name="Выживший", hp=120, attack_power=5)
player.add_item("Аптечка")

enemy = Character(name="Супермутант", hp=80, attack_power=15)

battle = Battle(player, enemy)
battle.start()
