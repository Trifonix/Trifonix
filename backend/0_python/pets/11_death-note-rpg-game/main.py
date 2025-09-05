import pygame
import sys
from player import Player
from enemy import Enemy
from game_map import GameMap
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Death Note RPG")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255) 

player = Player("Light Yagami")

enemies = [
    Enemy("Ryuk", 50, (3, 7)),
    Enemy("L", 60, (2, 8)),
    Enemy("Misa", 40, (1, 5))
]
current_enemy_index = 0
enemy = enemies[current_enemy_index]

game_map = GameMap()

font = pygame.font.Font(None, 32)
battle_log = []

def add_log(message, color=WHITE):
    battle_log.append((message, color))
    if len(battle_log) > 8:
        battle_log.pop(0)

def draw_log():
    y = 400
    for msg, color in battle_log:
        text = font.render(msg, True, color)
        screen.blit(text, (20, y))
        y += 25

def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        damage = player.attack_enemy()
        enemy.hp -= damage
        add_log(f"Player атакует {enemy.name} на {damage} HP", GREEN)

    if keys[pygame.K_s]:
        damage = player.death_note_attack()
        enemy.hp -= damage
        add_log(f"Player использует Death Note на {enemy.name}! -{damage} HP", BLUE)
    
    if random.random() < 0.02:
        damage = enemy.attack_player()
        player.hp -= damage
        add_log(f"{enemy.name} атакует Player на {damage} HP", RED)
    
    if enemy.hp <= 0:
        current_enemy_index += 1
        if current_enemy_index < len(enemies):
            enemy = enemies[current_enemy_index]
            add_log(f"Новый враг: {enemy.name}", WHITE)
        else:
            draw_text("Все враги побеждены! Победа!", 200, 300, GREEN)
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

    if player.hp <= 0:
        draw_text("Вы проиграли...", 300, 300, RED)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    draw_text(f"Локация: {game_map.current_location()}", 50, 20)
    draw_text(f"Player HP: {player.hp}", 50, 60)
    draw_text(f"Enemy: {enemy.name} HP: {enemy.hp}", 50, 100)
    draw_text("A - обычная атака | S - Death Note", 50, 200)

    draw_log()
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
