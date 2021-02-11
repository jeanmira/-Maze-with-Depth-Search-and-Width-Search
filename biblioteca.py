#------------------------------- /usr/bin/g++-7 ------------------------------#
#------------------------------- coding: utf-8 -------------------------------#
# Criado por:   Jean Marcelo Mira Junior
#               Victor Philos Donato Luiz da Silva
# Versão: 1.0
# Criado em: 11/02/2021
# Sistema operacional: Linux - Ubuntu 20.04.1 LTS

#------------------------------ Pacotes --------------------------------------#
import pygame
from random import randint
import numpy as np

#-----------------------------------------------------------------------------#


def Grafico(tabuleiro):
    # Inicializa o jogo
    pygame.init()

    # Inicializa e faz o set do tamanho do display
    tela = pygame.display.set_mode((400, 400))

    # Nome do Jogo
    pygame.display.set_caption("BFS/DFS - Labirinto")

    # Cria cores para
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)
    VERMELHO = (255, 0, 0)
    VERDE = (0, 255, 0)
    CINZA = (128, 128, 128)

    # Limitar os frames para nao ir muito rapido
    relogio = pygame.time.Clock()
    nivel = 6

    # Cria as variaveis para sair do jogo
    sair = True
    continuar = True

    # Jogo em si no laco de repeticao
    while sair:

        # Preenche o fundo com a cor escolhida
        tela.fill(BRANCO)

        while continuar:

            # Limita o frames portanto a velocidade do moviemnto (fps)
            relogio.tick(nivel)

            # Atualiza a tela
            pygame.display.update()
            # Le a tela do display
            for evento in pygame.event.get():
                # Se o usuario clicar no x fecha o display
                if evento.type == pygame.QUIT:
                    continuar = False

            linha = 0
            coluna = 0

            # Faz o tabuleiro
            for linha in range(10):
                for coluna in range(10):
                    if(tabuleiro[linha][coluna] == 0):
                        pygame.draw.rect(
                            tela, CINZA, (coluna * 40, linha * 40, 40, 40), 0)
                    elif (tabuleiro[linha][coluna] == 1):
                        pygame.draw.rect(
                            tela, BRANCO, (coluna * 40, linha * 40, 40, 40), 0)
                    elif (tabuleiro[linha][coluna] == 2):
                        pygame.draw.rect(
                            tela, VERDE, (coluna * 40, linha * 40, 40, 40), 0)
                    elif (tabuleiro[linha][coluna] == 3):
                        pygame.draw.rect(
                            tela, VERMELHO, (coluna * 40, linha * 40, 40, 40), 0)
                    pygame.draw.rect(
                        tela, PRETO, (coluna * 40, linha * 40, 40, 40), 3)

            # Atualiza a tela
            pygame.display.update()

        # Le a tela do display
        for evento in pygame.event.get():
            # Se o usuario clicar no x fecha o display
            if evento.type == pygame.QUIT:
                sair = False

    # Fecha o Jogo
    pygame.quit()
