import pygame
import random
import sys
import datetime
import math

pygame.init()
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Эволюция: Травоядные, Хищники и Ментаты")

# --- Цвета ---
BLACK = (14, 14, 14)
WHITE = (225, 225, 225)
GREEN = (0, 200, 0)     # растения
CYAN  = (100, 255, 100) # травоядные
RED   = (220, 50, 50)   # хищники
BLUE  = (50, 150, 255)  # ментаты

clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

# --- Текст ---
def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# --- Класс существа ---
class Creature:
    def __init__(self, x, y, speed, vision, color, species, size, shape):
        self.x = float(x)
        self.y = float(y)
        self.speed = speed
        self.vision = vision
        self.energy = 100
        self.color = color
        self.species = species
        self.size = size
        self.shape = shape

        angle = random.uniform(0, 2 * math.pi)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

    def move(self):
        # Плавное изменение направления
        if random.random() < 0.02:
            angle = random.uniform(0, 2 * math.pi)
            target_vx = math.cos(angle) * self.speed
            target_vy = math.sin(angle) * self.speed
            self.vx += (target_vx - self.vx) * 0.1
            self.vy += (target_vy - self.vy) * 0.1

        self.x += self.vx
        self.y += self.vy

        # Отражение от краёв
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

        self.energy -= 0.02 * self.speed

    def draw(self):
        pos = (int(self.x), int(self.y))

        if self.shape == "circle":
            pygame.draw.circle(screen, self.color, pos, self.size)

        elif self.shape == "triangle":
            points = [
                (self.x, self.y - self.size),
                (self.x - self.size, self.y + self.size),
                (self.x + self.size, self.y + self.size)
            ]
            pygame.draw.polygon(screen, self.color, points)

        elif self.shape == "diamond":
            points = [
                (self.x, self.y - self.size),
                (self.x - self.size, self.y),
                (self.x, self.y + self.size),
                (self.x + self.size, self.y)
            ]
            pygame.draw.polygon(screen, self.color, points)

        # Радиус зрения
        pygame.draw.circle(screen, (40, 40, 40), pos, self.vision, 1)

# --- Еда ---
foods = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(250)]

# --- Существа ---
creatures = []

# Травоядные
for _ in range(120):
    size = random.randint(5, 9)
    creatures.append(Creature(
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        speed=2,
        vision=60,
        color=CYAN,
        species="herbivore",
        size=size,
        shape="circle"
    ))

# Хищники
for _ in range(50):
    size = random.randint(7, 11)
    creatures.append(Creature(
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        speed=2.5,
        vision=80,
        color=RED,
        species="predator",
        size=size,
        shape="triangle"
    ))

# Ментаты
for _ in range(30):
    size = random.randint(6, 10)
    creatures.append(Creature(
        random.randint(0, WIDTH),
        random.randint(0, HEIGHT),
        speed=2,
        vision=100,
        color=BLUE,
        species="mentat",
        size=size,
        shape="diamond"
    ))

# --- Логика еды ---
def eat_logic(c, foods, creatures):
    if c.species == "herbivore":
        for f in foods[:]:
            if abs(c.x - f[0]) < 6 and abs(c.y - f[1]) < 6:
                foods.remove(f)
                c.energy += 40
                break

    elif c.species == "predator":
        for other in creatures[:]:
            if other.species == "herbivore" and abs(c.x - other.x) < 10 and abs(c.y - other.y) < 10:
                creatures.remove(other)
                c.energy += 80
                break
        for other in creatures[:]:
            if other.species == "mentat" and abs(c.x - other.x) < 10 and abs(c.y - other.y) < 10:
                creatures.remove(other)
                c.energy += 20
                break

    elif c.species == "mentat":
        for other in creatures[:]:
            if other.species == "predator" and abs(c.x - other.x) < 12 and abs(c.y - other.y) < 12:
                other.energy -= 50
                c.energy += 100
                break

# --- Размножение ---
def reproduce_logic(c, creatures):
    if c.energy > 200:
        new_speed = max(1, c.speed + random.choice([-0.5, 0, 0.5]))
        new_vision = max(20, c.vision + random.choice([-5, 0, 5]))
        new_size = max(4, c.size + random.choice([-1, 0, 1]))
        creatures.append(Creature(
            c.x, c.y, new_speed, new_vision, c.color,
            c.species, new_size, c.shape
        ))
        c.energy -= 100

# --- Время ---
start_time = pygame.time.get_ticks()

# --- Главный цикл ---
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random.random() < 0.1:
        foods.append((random.randint(0, WIDTH), random.randint(0, HEIGHT)))

    for f in foods:
        pygame.draw.circle(screen, GREEN, f, 4)

    for c in creatures[:]:
        c.move()
        eat_logic(c, foods, creatures)
        reproduce_logic(c, creatures)
        c.draw()
        if c.energy <= 0:
            creatures.remove(c)

    # --- Статистика ---
    elapsed_ms = pygame.time.get_ticks() - start_time
    elapsed_sec = elapsed_ms // 1000
    elapsed_min = elapsed_sec // 60
    elapsed_time = f"{elapsed_min:02}:{elapsed_sec % 60:02}"

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    herb_count = sum(1 for c in creatures if c.species == "herbivore")
    pred_count = sum(1 for c in creatures if c.species == "predator")
    ment_count = sum(1 for c in creatures if c.species == "mentat")

    stats_text1 = [
        f"Время симуляции: {elapsed_time}",
        f"Текущая дата: {now}",
    ]

    stats_text2 = [
        f"Травоядные: {herb_count}",
        f"Хищники: {pred_count}",
        f"Ментаты: {ment_count}"
    ]

    y = 10
    for line in stats_text1:
        draw_text(line, 10, y, WHITE)
        y += 25
    
    i = 0
    for line in stats_text2:
        color = [GREEN, RED, BLUE]
        draw_text(line, 10, y, color[i])
        i += 1
        y += 25

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
