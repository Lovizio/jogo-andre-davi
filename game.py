# game.py
import pygame
from config import *
from classes import Carro, Obstaculo
from imagens import background_image
from sons import *

def barra_vida(current_health):
    pygame.draw.rect(window, GREEN, (10, 10, 200 * (current_health / 5), 20))

def reset_game():
    global velocidade_obstaculo, timer_obstaculo, tempo_inicio, tempo_decorrido
    som_jogo.stop()
    som_jogo.play()
    velocidade_obstaculo = 5
    timer_obstaculo = 2000  # 2000 milissegundos = 2 segundos
    tempo_inicio = pygame.time.get_ticks()
    tempo_decorrido = tempo_inicio
    pygame.time.set_timer(pygame.USEREVENT + 1, timer_obstaculo)




def mostrar_menu():
    titulo = font.render('Aventura na Estrada', True, WHITE)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botao_start_rect.collidepoint(pygame.mouse.get_pos()):
                    reset_game()  # Reinicia o jogo antes de começar
                    main_game()
                if fechar.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    exit()

        window.fill(BLACK)
        window.blit(background_image, (0, 0))
        window.blit(titulo, titulo_rect)
        window.blit(botao_start, botao_start_rect)
        window.blit(fecharbotao, fechar)
        pygame.display.flip()
        clock.tick(15)




def mostrar_game_over(tempo_decorrido):
    # 'game over' na tela
    texto_game_over = font.render('GAME OVER', True, WHITE)
    # texto mostrando o tempo o jogador ficou vivo
    texto_score = font.render(f'Você ficou vivo {tempo_decorrido:.2f} segundos', True, WHITE)
    
    # posição do texto 'GAME OVER' na tela
    game_over_rect = texto_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    # posição do texto do score na tela
    score_rect = texto_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))
    
    # tela com a cor preta
    window.fill(BLACK)
    # 'game over' na tela
    window.blit(texto_game_over, game_over_rect)
    # score na tela
    window.blit(texto_score, score_rect)
    # Atualiza 
    pygame.display.flip()
    # 5 segundos antes de voltar ao menu
    pygame.time.wait(5000)
    # mostrar o menu
    mostrar_menu()

def main_game():
    global velocidade_obstaculo, timer_obstaculo, tempo_inicio, tempo_decorrido
    reset_game()
    carro = Carro()
    obstaculos = pygame.sprite.Group()
    pontos = 5  # vida

    running = True
    ultimo_aumento = 0  # velocidade foi aumentada pela última vez

    while running:
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - tempo_inicio) / 1000

        # Aumenta a velocidade dos obstáculos a cada 5 segundos
        if elapsed_time - ultimo_aumento >= 5:  # Verifica se já passaram 10 segundos desde o último aumento
            velocidade_obstaculo += 1
            ultimo_aumento = elapsed_time  # Atualiza 

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT + 1:
                novo_obstaculo = Obstaculo(velocidade_obstaculo)
                obstaculos.add(novo_obstaculo)

        if pygame.sprite.spritecollide(carro, obstaculos, True, pygame.sprite.collide_mask):
            pontos -= 1
            if pontos <= 0:
                mostrar_game_over(elapsed_time)
                return  # mostrar a tela de Game Over

        carro.update(keys)
        obstaculos.update()

        window.blit(background_image, (0, 0))
        window.blit(carro.image, carro.rect)
        obstaculos.draw(window)
        barra_vida(pontos)

        timer_text = timer_font.render(f"Tempo: {elapsed_time:.2f} s", True, WHITE)
        window.blit(timer_text, (10, 50))

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    exit()
mostrar_menu()  # Inicializa com o menu principal