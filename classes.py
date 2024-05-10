# classes.py
import pygame
import random
from config import *
from imagens import *


#Classe do carro:
class Carro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.transform.scale(car_image, (150, 150)), 270)#Rotacionando para virar o carro na direcao certa
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 100))#Definindo o retângulo que esta port volta da imagem.
        self.speed = 5 #Velocidade do carro


