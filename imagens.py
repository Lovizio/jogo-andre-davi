# imagens.py
import pygame

def load_image(path):
    return pygame.image.load(path)

car_image = load_image('assets/Desenho_Carro copy.png')
cone_image = load_image('assets/ConeAnimadoADOBE copy.png')
background_image = load_image('assets/BACK_ESTRADA_CIMA.png')  # Carregando a imagem de fundo

