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


def mostrar_menu():
    titulo = font.render('Jogo de Corrida com Obstáculos', True, WHITE)
    botao_start = font.render('Iniciar', True, WHITE)
    fecharbotao = font.render('Sair', True, WHITE)

    titulo_rect = titulo.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    botao_start_rect = botao_start.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    fechar = fecharbotao.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    menu_ativo = True
    while menu_ativo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
def main_game():
    global velocidade_obstaculo, timer_obstaculo, tempo_inicio, tempo_decorrido
    reset_game()
    carro = Carro()
    obstaculos = pygame.sprite.Group()
    pontos = 5  # Inicializa as vidas

    running = True
    while running:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - tempo_inicio) / 1000

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT + 1:
                novo_obstaculo = Obstaculo(velocidade_obstaculo)
                obstaculos.add(novo_obstaculo)
