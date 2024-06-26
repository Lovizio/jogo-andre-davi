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
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 100))#Definindo o retângulo que esta por volta da imagem.
        self.speed = 5 #Velocidade do carro


    def update(self, keys):
            # Ver se a tecla da seta para esquerda foi apertada
            if keys[pygame.K_LEFT]:
            # Ver o limite
                if self.rect.left > 0:
                # Mover para a esquerda
                    self.rect.x -= self.speed

        # Verifica se a tecla da seta para direita foi apertada
            if keys[pygame.K_RIGHT]:
            # Ver o limite
                if self.rect.right < WIDTH:
                # Move para a direita
                    self.rect.x += self.speed

        # Ver se a tecla da seta para cima foi apertada
            if keys[pygame.K_UP]:
            # Ver o limite
                if self.rect.top > 0:
                # Move para cima
                    self.rect.y -= self.speed

        # Ver se a tecla da seta para baixo foi apertada
            if keys[pygame.K_DOWN]:
            # Ver o limite
                if self.rect.bottom < HEIGHT:
                # Move para baixo
                    self.rect.y += self.speed

# Classe Obstaculo 
class Obstaculo(pygame.sprite.Sprite):
    #parâmetro 'speed' define a velocidade do obstáculo
    def __init__(self, speed):
        super().__init__()  #inicialização correta
        self.image = pygame.transform.scale(cone_image, (50, 50))  # imagem do obstáculo
        # 'x' é largura da tela (começando fora dela), e 'y' uma posição aleatória 
        self.rect = self.image.get_rect(x=WIDTH, y=random.randint(50, HEIGHT - 50))
        self.speed = speed  # velocidade do obstáculo
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()