# config.py
import pygame

# Constantes
WIDTH, HEIGHT = 800, 370
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Inicializações do Pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo de Corrida com Obstáculos')
clock = pygame.time.Clock()
FPS = 60
font = pygame.font.Font(None, 36)
timer_font = pygame.font.Font(None, 48)