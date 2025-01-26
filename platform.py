import main
import random
import pygame
from settings import screen_width, screen_height, screen, brown, chicken_velocity_y

brown = (139, 69, 19)         # Цвет для платформ

# Настройки платформ

platform_width = 120
platform_height = 15
platforms = []

# Функция для создания новой платформы
def create_platform():
    x = random.randint(0, screen_width - platform_width)
    y = platforms[-1][1] - random.randint(80, 120) if platforms else screen_height - 50
    platforms.append((x, y))

# Создаем начальные платформы
for _ in range(5):
    create_platform()

# Функция для рисования платформы
def draw_platform(x, y):
    pygame.draw.rect(screen, brown, (x, y, platform_width, platform_height))

# Функция для проверки коллизий с платформами
def check_collision(rect, platforms):
    for platform in platforms:
        platform_rect = pygame.Rect(platform[0], platform[1], platform_width, platform_height)
        if rect.colliderect(platform_rect) and chicken_velocity_y >= 0:
            return platform_rect
    return None

    # Рисование платформ
for platform in platforms:
    draw_platform(platform[0], platform[1])

    # Удаление платформ, которые ушли за пределы экрана
    platforms = [platform for platform in platforms if platform[1] < screen_height]

    # Создание новых платформ
    while len(platforms) < 5:
        create_platform()
