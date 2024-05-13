# game.py
import pygame
from config import *
from classes import Carro, Obstaculo
from imagens import background_image

def barra_vida(current_health):
    pygame.draw.rect(window, GREEN, (10, 10, 200 * (current_health / 5), 20))

