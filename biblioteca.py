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
import time

#-----------------------------------------------------------------------------#


def Dfs(tabuleiro, linha, coluna):
    caminho = [(linha, coluna), (linha, coluna)]
    repeticao = 0
    contador = 1
    final = False
    no = False

    identificaNo = []

    # Faz ate encontrar o 3
    while (final != True):

        # ---------------------------------------------------
        # print(caminho[contador-2], (linha+1, coluna), "\n")
        # print(caminho)
        # print(identificaNo, "\n")
        # ---------------------------------------------------

        # Gera numero aleatorio de 1 a 4 para determinar qual posicao aleatoria ele deve entrar
        # Serve para o agente nao entrar e seguir na mesma posicao infinitamente
        acesso = randint(1, 4)

        # -----------------------
        # Funcoes sucessor
        # -----------------------

        # Verifica para baixo
        if(acesso == 1 and linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha + 1][coluna] == 0):
            # If inicialmente criado para nao deixar o agente voltar a posicao anterior, a nao ser que entre em um caminho sem volta
            # if(caminho[contador-2] != (linha+1, coluna) or repeticao > 2):
            linha += 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            repeticao = 0

        # ----------------------
        # Teste de Objetivo
        # ----------------------

        if (tabuleiro[linha + 1][coluna] == 3):
            linha += 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            final = True

        # -----------------------
        # Funcoes sucessor
        # -----------------------

        # Veridica para a esquerda
        if(acesso == 2 and linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha][coluna - 1] == 0):
            # If inicialmente criado para nao deixar o agente voltar a posicao anterior, a nao ser que entre em um caminho sem volta
            # if (caminho[contador-2] != (linha, coluna-1) or repeticao > 2):
            coluna -= 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            repeticao = 0

        # ----------------------
        # Teste de Objetivo
        # ----------------------

        if (tabuleiro[linha][coluna - 1] == 3):
            coluna -= 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            final = True

        # -----------------------
        # Funcoes sucessor
        # -----------------------

        # Veridica para a direita
        if(acesso == 3 and linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha][coluna + 1] == 0):
            # If inicialmente criado para nao deixar o agente voltar a posicao anterior, a nao ser que entre em um caminho sem volta
            # if (caminho[contador-2] != (linha, coluna+1) or repeticao > 2):
            coluna += 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            repeticao = 0

        # ----------------------
        # Teste de Objetivo
        # ----------------------

        if (tabuleiro[linha][coluna + 1] == 3):
            coluna += 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            final = True

        # -----------------------
        # Funcoes sucessor
        # -----------------------

        # Verifica para cima
        if(acesso == 4 and linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha - 1][coluna] == 0):
            # If inicialmente criado para nao deixar o agente voltar a posicao anterior, a nao ser que entre em um caminho sem volta
            # if(caminho[contador-2] != (linha-1, coluna) or repeticao > 2):
            linha -= 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            repeticao = 0

        # ----------------------
        # Teste de Objetivo
        # ----------------------

        if (tabuleiro[linha-1][coluna] == 3):
            linha -= 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            final = True

        repeticao += 1
        # time.sleep(1)

    return(caminho, final)


def interacoes(caminho):
    return len(caminho)


def Grafico(tabuleiro):
    # Inicializa o jogo
    pygame.init()

    # Velocidade da demonstracao
    Velocidade = 0.01

    # Inicializa e faz o set do tamanho do display
    tela = pygame.display.set_mode((397, 397))

    resultado = False

    # Nome do Jogo
    pygame.display.set_caption("DFS - Labirinto")

    # Cria cores para
    BRANCO = (255, 255, 255)
    PRETO = (0, 0, 0)
    VERMELHO = (255, 0, 0)
    VERDE = (0, 255, 0)
    CINZA = (128, 128, 128)
    AMARELO = (255, 255, 0)

    # Limitar os frames para nao ir muito rapido
    relogio = pygame.time.Clock()
    nivel = 10

    # Cria as variaveis para sair do jogo
    sair = True
    continuar = True

    # Jogo em si no laco de repeticao
    while sair:

        # Preenche o fundo com a cor escolhida
        tela.fill(BRANCO)

        # Limita o frames portanto a velocidade do moviemnto (fps)
        relogio.tick(nivel)

        while continuar:
            # Atualiza a tela
            pygame.display.update()

            # Le a tela do display
            for evento in pygame.event.get():
                # Se o usuario clicar no x fecha o display
                if evento.type == pygame.QUIT:
                    caminho = False
            # ----------------------------------------------------------------------------
            # Bloco da parte grafica inicial
            # ----------------------------------------------------------------------------
            linha = 0
            coluna = 0

            # Faz o tabuleiro - obs: tem borda por isso -1
            for linha in range(1, 11):
                for coluna in range(1, 11):
                    if(tabuleiro[linha][coluna] == 1):
                        pygame.draw.rect(
                            tela, CINZA, ((coluna - 1) * 40, (linha - 1) * 40, 37, 37), 0)
                    elif (tabuleiro[linha][coluna] == 0):
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

            # ----------------------------------------------------------------------------
            # Bloco da analise e da parte grafica depois da analise
            # ----------------------------------------------------------------------------
            if(resultado == False):
                # Onde o agente inicializa
                caminho, resultado = Dfs(tabuleiro, 1, 1)

            # Imprimi toda parte final da analise
            else:
                print("Custo de Etapa Total:", interacoes(caminho))

                for i in range(len(caminho)):
                    lin, col = caminho[i]
                    # print(col, lin, i)

                    # Le a tela do display
                    for evento in pygame.event.get():
                        # Se o usuario clicar no x fecha o display
                        if evento.type == pygame.QUIT:
                            caminho = False

                    for linha in range(1, 11):
                        for coluna in range(1, 11):
                            if(tabuleiro[linha][coluna] == 1):
                                pygame.draw.rect(
                                    tela, CINZA, ((coluna - 1) * 40, (linha - 1) * 40, 37, 37), 0)

                            elif (tabuleiro[linha][coluna] == 0):
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

                            pygame.draw.rect(
                                tela, AMARELO, ((col - 1) * 40, (lin - 1) * 40, 37, 37), 0)

                    # Para demonstrar mais lento
                    time.sleep(Velocidade)

                    # Atualiza a tela
                    pygame.display.update()

                continuar = False

        # Le a tela do display
        for evento in pygame.event.get():
            # Se o usuario clicar no x fecha o display
            if evento.type == pygame.QUIT:
                sair = False

    # Fecha o Jogo
    pygame.quit()
