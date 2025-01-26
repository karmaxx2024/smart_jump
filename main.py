from settings import *
from player import *
from platform import *
from objects import *
import sys
import pygame

white = (255, 255, 255)# Цвет фона

# Инициализация Pygame
pygame.init()

# Очистка экрана
screen.fill(white)

# Завершение работы
pygame.quit()
sys.exit()