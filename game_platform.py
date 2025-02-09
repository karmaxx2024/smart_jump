import pygame  # Импорт библиотеки Pygame для работы с графикой и событиями
import random  # Импорт модуля random для генерации случайных чисел (например, для расположения платформ)
from settings import screen, screen_width, screen_height, brown  # Импортируем настройки игры, такие как размеры экрана, цвета и гравитация

platform_width = 60
platform_height = 15

# Используем глобальный список платформ
platforms = []

def log_debug(text):
    with open("debug.txt", "a") as f:
        f.write(text + "\n")

def create_platform():
    global platforms
    x = random.randint(0, screen_width - platform_width)
    y = platforms[-1][1] - random.randint(80, 120) if platforms else screen_height - 50
    platforms.append((x, y))
    print(f"Создана платформа: ({x}, {y})")
    log_debug(f"Создана платформа: ({x}, {y})")

def create_starting_platforms():
    global platforms
    for i in range(5):
        create_platform()
    log_debug(f"Итоговый список платформ: {platforms}")

def get_platforms():
    return platforms

def draw_platform(x, y):
    pygame.draw.rect(screen, brown, (x, y, platform_width, platform_height))

def check_collision(rect):
    global platforms
    for platform in platforms:
        platform_rect = pygame.Rect(platform[0], platform[1], platform_width, platform_height)
        if rect.colliderect(platform_rect):
            return platform_rect
    return None
