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


def VerificaNo(identificaNo, tabuleiro, col, lin):
    # Verifica se tem 3 nos
    if (lin > 0 and lin < 10 and col > 0 and col < 10 and tabuleiro[lin][col - 1] == 0 and tabuleiro[lin][col + 1] == 0 and tabuleiro[lin + 1][col] == 0):
        identificaNo.append((lin, col))
        identificaNo.append((lin, col-1))
        identificaNo.append((lin, col+1))
        identificaNo.append((lin+1, col))
        no = True

        semSaida = False

        contador = 1
        final = False

        i = 1
        controle = False

        # Faz ate encontrar o 3
        while (final != True or i != 3):

            if (controle == False):
                linha, coluna = identificaNo[i]
                controle = True
                caminho = [identificaNo[i], identificaNo[i]]

            # Verifica para baixo
            if(linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and (linha+1, coluna) != identificaNo[0] and tabuleiro[linha + 1][coluna] == 0 and caminho[contador-2] != (linha+1, coluna)):
                linha += 1
                caminho.append((linha, coluna))
                contador = len(caminho)

            if (tabuleiro[linha + 1][coluna] == 3):
                linha += 1
                caminho.append((linha, coluna))
                contador = len(caminho)
                final = True

            # Efetua recursividade caso o objeto tenha um novo no
            VerificaNo(identificaNo, tabuleiro, coluna, linha)

            # Veridica para a esquerda
            if(linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and (linha, coluna-1) != identificaNo[0] and tabuleiro[linha][coluna - 1] == 0 and caminho[contador-2] != (linha, coluna-1)):
                coluna -= 1
                caminho.append((linha, coluna))
                contador = len(caminho)

            if (tabuleiro[linha][coluna - 1] == 3):
                coluna -= 1
                caminho.append((linha, coluna))
                contador = len(caminho)
                final = True

            # Veridica para a direita
            if(linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and (linha, coluna+1) != identificaNo[0] and tabuleiro[linha][coluna + 1] == 0 and caminho[contador-2] != (linha, coluna+1)):
                coluna += 1
                caminho.append((linha, coluna))
                contador = len(caminho)

            if (tabuleiro[linha][coluna + 1] == 3):
                coluna += 1
                caminho.append((linha, coluna))
                contador = len(caminho)
                final = True

            # Verifica para cima
            if(linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and (linha-1, coluna) != identificaNo[0] and tabuleiro[linha - 1][coluna] == 0 and caminho[contador-2] != (linha-1, coluna)):
                linha -= 1
                caminho.append((linha, coluna))
                contador = len(caminho)

            if (tabuleiro[linha-1][coluna] == 3):
                linha -= 1
                caminho.append((linha, coluna))
                contador = len(caminho)
                final = True

            # Verifica se esta sem saida so podendo voltar por onde venho
            if(tabuleiro[linha][coluna+1] != 1 and tabuleiro[linha+1][coluna] != 0 and tabuleiro[linha-1][coluna] != 0 and tabuleiro[linha][coluna-1] != 0):
                semSaida = True
            if(tabuleiro[linha][coluna+1] != 0 and tabuleiro[linha+1][coluna] != 1 and tabuleiro[linha-1][coluna] != 0 and tabuleiro[linha][coluna-1] != 0):
                semSaida = True
            if(tabuleiro[linha][coluna+1] != 0 and tabuleiro[linha+1][coluna] != 0 and tabuleiro[linha-1][coluna] != 1 and tabuleiro[linha][coluna-1] != 0):
                semSaida = True
            if(tabuleiro[linha][coluna+1] != 0 and tabuleiro[linha+1][coluna] != 0 and tabuleiro[linha-1][coluna] != 0 and tabuleiro[linha][coluna-1] != 1):
                semSaida = True

            # Parte principal responsavel por reiniciar a busca caso o caminho nao de em nada
            if ((linha-1, coluna) == identificaNo[0] or semSaida == True):
                i += 1
                contador = 1
                controle = False
                semSaida = False

            if(tabuleiro[linha][coluna] == 3):
                return (caminho, True)

            # time.sleep(1)
    else:
        return (0, False)


def Dfs(tabuleiro, linha, coluna):
    caminho = [(linha, coluna), (linha, coluna)]

    contador = 1
    final = False
    no = False

    identificaNo = []

    # Faz ate encontrar o 3
    while (final != True):

        #print(identificaNo, "\n")

        print(caminho)
        # Verifica para baixo
        if(linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha + 1][coluna] == 0 and caminho[contador-2] != (linha+1, coluna)):
            linha += 1
            caminho.append((linha, coluna))
            contador = len(caminho)

        if (tabuleiro[linha + 1][coluna] == 3):
            linha += 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            final = True

        # Funcao que verifica se ha algum no, se tiver entra e ela faz a analise de busca
        vetorNo, resposta = VerificaNo(identificaNo, tabuleiro, coluna, linha)

        if resposta == True:
            for i in range(len(vetorNo)):
                if i != 0:
                    caminho.append(vetorNo[i])
            final = True
            print(caminho)
            return(caminho, final)

        # Veridica para a esquerda
        if(linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha][coluna - 1] == 0 and caminho[contador-2] != (linha, coluna-1)):
            coluna -= 1
            caminho.append((linha, coluna))
            contador = len(caminho)

        if (tabuleiro[linha][coluna - 1] == 3):
            coluna -= 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            final = True

        # Veridica para a direita
        if(linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha][coluna + 1] == 0 and caminho[contador-2] != (linha, coluna+1)):
            coluna += 1
            caminho.append((linha, coluna))
            contador = len(caminho)

        if (tabuleiro[linha][coluna + 1] == 3):
            coluna += 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            final = True

        # Verifica para cima
        if(linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha - 1][coluna] == 0 and caminho[contador-2] != (linha-1, coluna)):
            linha -= 1
            caminho.append((linha, coluna))
            contador = len(caminho)

        if (tabuleiro[linha-1][coluna] == 3):
            linha -= 1
            caminho.append((linha, coluna))
            contador = len(caminho)
            final = True
        # time.sleep(1)

    return(caminho, final)


def Grafico(tabuleiro):
    # Inicializa o jogo
    pygame.init()

    # Inicializa e faz o set do tamanho do display
    tela = pygame.display.set_mode((397, 397))

    resultado = False

    # Nome do Jogo
    pygame.display.set_caption("BFS/DFS - Labirinto")

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

            if(resultado == False):
                caminho, resultado = Dfs(tabuleiro, 1, 1)
                # print(caminho)

            # Imprimi toda parte final da analise
            else:
                for i in range(len(caminho)):
                    lin, col = caminho[i]
                    # print(col, lin, i)

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
                    time.sleep(0.2)
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
