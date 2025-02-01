


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() # Вызов конструктора родительского класса (повторить констуркторы)
        self.image = pygame.image.load(PLAYER_).convert_alpha()
        self.rect = self.image.get_rect() # получаем прямоугольник для изображения
        self.rect.centre = (x, y)
        self.vel_y = 0
        self.vel_x = 0
        self.score = 0

        self.jump_sound = pygame.mixer.Sound(SOUND_JUMP) # загружаем звук прыжка
        self.jump_sound.set_volume()

# Функция для рисования курицы
def draw_chicken(x, y):
    # Тело курицы (маленький эллипс)
    pygame.draw.ellipse(screen, yellow, (x - 15, y - 25, 30, 40))
    # Голова курицы (круг)
    pygame.draw.circle(screen, yellow, (x, y - 35), 10)
    # Глаза (два маленьких круга)
    pygame.draw.circle(screen, black, (x - 5, y - 37), 3)
    pygame.draw.circle(screen, black, (x + 5, y - 37), 3)
    # Клюв (треугольник)
    pygame.draw.polygon(screen, orange, [(x - 5, y - 32), (x + 5, y - 32), (x, y - 27)])
    # Лапы (две линии)
    pygame.draw.line(screen, orange, (x - 7, y + 15), (x - 12, y + 25), 3)
    pygame.draw.line(screen, orange, (x + 7, y + 15), (x + 12, y + 25), 3)

# Позиция и параметры курицы
chicken_x = screen_width // 2
chicken_y = screen_height - 100
chicken_width = 30
chicken_height = 40
chicken_velocity_y = 0  # Скорость по вертикали
chicken_velocity_x = 0  # Скорость по горизонтали
gravity = 0.8  # Гравитация
jump_speed = -15  # Скорость прыжка
horizontal_speed = 5  # Скорость движения влево/вправо
on_ground = True  # Находится ли курица на земле или платформе
score = 0  # Счет

# Применение гравитации
chicken_velocity_y += gravity
chicken_y += chicken_velocity_y

# Применение горизонтального движения
chicken_x += chicken_velocity_x

# Проверка коллизий с платформами
chicken_rect = pygame.Rect(chicken_x - 15, chicken_y - 25, chicken_width, chicken_height)
platform_collided = check_collision(chicken_rect, platforms)

if platform_collided:
    chicken_y = platform_collided.top - chicken_height // 2
    chicken_velocity_y = 0
    on_ground = True

# Проверка коллизии с землей
if chicken_y + chicken_height // 2 >= screen_height - 50:
    chicken_y = screen_height - 50 - chicken_height // 2
    chicken_velocity_y = 0
    on_ground = True

# Ограничение движения курицы по горизонтали
if chicken_x < 0:
    chicken_x = 0
if chicken_x > screen_width:
    chicken_x = screen_width

# Прокрутка платформ вниз, если курица поднимается
if chicken_y < screen_height // 2:
    scroll = screen_height // 2 - chicken_y
    chicken_y += scroll
    for i in range(len(platforms)):
        platforms[i] = (platforms[i][0], platforms[i][1] + scroll)
    score += 1  # Увеличиваем счет на 1 за каждую прокрутку

# Рисование курицы
draw_chicken(chicken_x, chicken_y)
