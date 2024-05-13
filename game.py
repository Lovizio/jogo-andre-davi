# game.py
import pygame
from config import *
from classes import Carro, Obstaculo
from imagens import background_image

def barra_vida(current_health):
    pygame.draw.rect(window, GREEN, (10, 10, 200 * (current_health / 5), 20))

def reset_game():
    global velocidade_obstaculo, timer_obstaculo, tempo_inicio, tempo_decorrido
    velocidade_obstaculo = 5
    timer_obstaculo = 2000  # 2000 milissegundos = 2 segundos
    tempo_inicio = pygame.time.get_ticks()
    tempo_decorrido = tempo_inicio
    pygame.time.set_timer(pygame.USEREVENT + 1, timer_obstaculo)