import sys  # Импортируем sys для выхода из игры при закрытии окна
import pygame  # Импорт библиотеки Pygame для работы с графикой и событиями
import random  # Импорт модуля random для генерации случайных чисел (например, для расположения платформ)
from settings import screen, white, screen_width, screen_height  # Импортируем настройки игры, такие как размеры экрана, цвета и гравитация
from objects import draw_objects  # Импортируем вспомогательные функции для рисования объектов на экране
import game_platform  # Импортируем весь модуль
from player import Player  # Импортируем класс игрока и его функции (движение, прыжки, отрисовка)

pygame.init()

def log_debug(text):
    with open("debug.txt", "a") as f:
        f.write(text + "\n")


game_platform.create_starting_platforms()
platforms = game_platform.get_platforms()


log_debug(f"🔹 Платформы в начале игры: {platforms}")
print(f"🔹 Платформы в начале игры: {len(platforms)}")

# Создаем игрока
player = Player(screen_width // 2, screen_height - 100)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    # Скроллинг экрана вверх при прыжке
    if player.rect.top < screen_height // 2:
        scroll = screen_height // 2 - player.rect.top
        player.rect.y += scroll
        for i in range(len(platforms)):
            platforms[i] = (platforms[i][0], platforms[i][1] + scroll)

        # Создаём новую платформу, если самая верхняя ушла слишком далеко
        if platforms and platforms[-1][1] > 100:
            game_platform.create_platform()

    if len(platforms) == 0:
        log_debug("❌ Ошибка! Список platforms был обнулён!")
        print("❌ Ошибка! Список platforms был обнулён!")
        game_platform.create_starting_platforms()
        platforms = game_platform.get_platforms()

    # Удаление платформ, вышедших за нижний край экрана
    platforms[:] = [p for p in platforms if p[1] < screen_height]

    log_debug(f"🔹 Платформы на экране после проверки: {platforms}")
    print(f"🔹 Платформы на экране после проверки: {len(platforms)}")

    # Отрисовка объектов
    draw_objects()
    for platform in platforms:
        game_platform.draw_platform(platform[0], platform[1])
    player.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
