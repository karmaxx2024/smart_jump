import main

# Настройки экрана (разрешение как у смартфона в портретном режиме)
screen_width, screen_height = 360, 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Smart Jump')

# Цвета
light_blue = (173, 216, 230)  # Цвет для облаков
white = (255, 255, 255)       # Цвет фона
green = (34, 139, 34)         # Цвет для земли
brown = (139, 69, 19)         # Цвет для платформ
yellow = (255, 255, 0)        # Цвет для курицы
orange = (255, 165, 0)        # Цвет для клюва и лап
black = (0, 0, 0)             # Цвет для глаз


# Основной игровой цикл
running = True
clock = pygame.time.Clock()  # Добавляем часы для контроля FPS

# Счет и рекорд
score = 0
high_score = 0

# Загрузка рекорда из файла
try:
    with open("high_score.txt", "r") as file:
        high_score = int(float(file.read()))  # Преобразуем в float, затем в int
except FileNotFoundError:
    high_score = 0

# Основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:  # Прыжок
                chicken_velocity_y = jump_speed
                on_ground = False
            if event.key == pygame.K_LEFT:  # Движение влево
                chicken_velocity_x = -horizontal_speed
            if event.key == pygame.K_RIGHT:  # Движение вправо
                chicken_velocity_x = horizontal_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # Остановка при отпускании клавиш
                chicken_velocity_x = 0

 # Обновление рекорда
    if score > high_score:
        high_score = int(round(score))  # Округляем счет до целого числа
        with open("high_score.txt", "w") as file:
            file.write(str(high_score))  # Сохраняем целое число

    # Отображение счета и рекорда
    font = pygame.font.SysFont("Arial", 24)
    score_text = font.render(f"Счет: {score}", True, black)
    high_score_text = font.render(f"Рекорд: {high_score}", True, black)
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 40))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)