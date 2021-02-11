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
import collections

#-----------------------------------------------------------------------------#


def Dfs(tabuleiro, linha, coluna):
    caminho = [(linha, coluna)]
    identificaNo = []

    # Faz ate encontrar o 3
    while (tabuleiro[linha][coluna] != 3):
        # Verifica se tem 3 nos
        if (linha > 0 and linha < 10 and coluna >= 0 and coluna < 10 and tabuleiro[linha][coluna - 1] == 1 and tabuleiro[linha][coluna + 1] == 1 and tabuleiro[linha + 1][coluna] == 1):
            identificaNo.append((linha, coluna-1))
            identificaNo.append((linha+1, coluna))
            identificaNo.append((linha, coluna+1))

        # Verifica se tem 2 nos
        elif (linha >= 0 and linha < 10 and coluna >= 0 and coluna < 10 and tabuleiro[linha][coluna - 1] == 1 and tabuleiro[linha][coluna + 1] == 1):
            identificaNo.append((linha, coluna-1))
            identificaNo.append((linha+1, coluna))

        elif (linha >= 0 and linha < 10 and coluna >= 0 and coluna < 10 and tabuleiro[linha + 1][coluna] == 1 and tabuleiro[linha][coluna + 1] == 1):
            identificaNo.append((linha+1, coluna))
            identificaNo.append((linha, coluna+1))

        elif (linha >= 0 and linha < 10 and coluna >= 0 and coluna < 10 and tabuleiro[linha - 1][coluna] == 1 and tabuleiro[linha][coluna + 1] == 1):
            identificaNo.append((linha-1, coluna))
            identificaNo.append((linha, coluna+1))

        # Verifica para baixo
        if(linha >= 0 and linha < 10 and coluna >= 0 and coluna < 10 and tabuleiro[linha + 1][coluna] == 1):
            linha += 1
            caminho.append((linha, coluna))
        # Veridica para a direita
        if(linha >= 0 and linha < 10 and coluna >= 0 and coluna < 10 and tabuleiro[linha][coluna + 1] == 1):
            coluna += 1
            caminho.append((linha, coluna))
        # Veridica para a direita
        if(linha >= 0 and linha < 10 and coluna >= 0 and coluna < 10 and tabuleiro[linha][coluna + 1] == 1):
            coluna += 1
            caminho.append((linha, coluna))

        print(caminho)
        print(identificaNo)
    return(caminho)


def Grafico(tabuleiro):
    # Inicializa o jogo
    pygame.init()

    # Inicializa e faz o set do tamanho do display
    tela = pygame.display.set_mode((397, 397))

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

    # Jogo em si no laco de repeticao
    while sair:

        # Preenche o fundo com a cor escolhida
        tela.fill(BRANCO)

        # Limita o frames portanto a velocidade do moviemnto (fps)
        relogio.tick(nivel)

        # Atualiza a tela
        pygame.display.update()

        linha = 0
        coluna = 0

        # Faz o tabuleiro - obs: tem borda por isso -1
        for linha in range(1, 11):
            for coluna in range(1, 11):
                if(tabuleiro[linha][coluna] == 0):
                    pygame.draw.rect(
                        tela, CINZA, ((coluna - 1) * 40, (linha - 1) * 40, 37, 37), 0)
                elif (tabuleiro[linha][coluna] == 1):
                    pygame.draw.rect(
                        tela, BRANCO, ((coluna - 1) * 40, (linha - 1) * 40, 37, 37), 0)
                elif (tabuleiro[linha][coluna] == 2):
                    pygame.draw.rect(
                        tela, VERDE, ((coluna - 1) * 40, (linha - 1) * 40, 37, 37), 0)
                elif (tabuleiro[linha][coluna] == 3):
                    pygame.draw.rect(
                        tela, VERMELHO, ((coluna - 1) * 40, (linha - 1) * 40, 37, 37), 0)
                pygame.draw.rect(
                    tela, PRETO, ((coluna - 1) * 40, (linha - 1) * 40, 37, 37), 3)

        # Atualiza a tela
        pygame.display.update()

        caminho = Dfs(tabuleiro, 1, 1)
        print(caminho)

        # Le a tela do display
        for evento in pygame.event.get():
            # Se o usuario clicar no x fecha o display
            if evento.type == pygame.QUIT:
                sair = False

    # Fecha o Jogo
    pygame.quit()
