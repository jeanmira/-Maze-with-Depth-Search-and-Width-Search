#------------------------------- /usr/bin/g++-7 ------------------------------#
#------------------------------- coding: utf-8 -------------------------------#
# Criado por:   Jean Marcelo Mira Junior
#               Victor Philos Donato Luiz da Silva
# Versão: 2.0
# Criado em: 23/02/2021
# Sistema operacional: Linux - Ubuntu 20.04.1 LTS
# Python 3
#------------------------------ Pacotes --------------------------------------#
import pygame
from random import randint
import time
#-----------------------------------------------------------------------------#
def Teste_de_Objetrivo_Dfs(tabuleiro, linha, coluna):
   if(linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10):
       if (tabuleiro[linha + 1][coluna] == 3):
           return (True, 1)
       elif (tabuleiro[linha][coluna - 1] == 3):
           return (True, 2)
       elif (tabuleiro[linha][coluna + 1] == 3):
           return (True, 3)
       elif (tabuleiro[linha-1][coluna] == 3):
           return (True, 4)
       else:
           return (False, 0)
  
 
def Sucessor_Dfs(tabuleiro, linha, coluna):
   caminho = [(linha, coluna), (linha, coluna)]
   repeticao = 0
   final = False
   teste = False
   chave = 0
 
   # Faz até encontrar o 3
   while (final != True):
 
       # Gerar número aleatório de 1 a 4 para determinar qual posição aleatória ele deve entrar junto com o if abaixo
       acesso = randint(1, 4)
 
       # -----------------------
       # Funções sucessor
       # -----------------------
 
       # Verifica para baixo
       if(acesso == 1 and linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha + 1][coluna] == 0):
           linha += 1
           caminho.append((linha, coluna))
           repeticao = 0
 
       # ----------------------
       # Chama o teste de Objetivo
       # ----------------------
       teste, chave = Teste_de_Objetrivo_Dfs(tabuleiro, linha, coluna)
       if (teste == True and chave == 1):
           linha += 1
           caminho.append((linha, coluna))
           final = True
 
       # -----------------------
       # Funções sucessor
       # -----------------------
 
       # Verídica para a esquerda
       if(acesso == 2 and linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha][coluna - 1] == 0):
           coluna -= 1
           caminho.append((linha, coluna))
           repeticao = 0
 
       # ----------------------
       # Chama o teste de Objetivo
       # ----------------------
       teste, chave = Teste_de_Objetrivo_Dfs(tabuleiro, linha, coluna)
       if (teste == True and chave == 2):
           coluna -= 1
           caminho.append((linha, coluna))
           final = True
 
       # -----------------------
       # Funções sucessor
       # -----------------------
 
       # Verídica para a direita
       if(acesso == 3 and linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha][coluna + 1] == 0):
           coluna += 1
           caminho.append((linha, coluna))
           repeticao = 0
 
       # ----------------------
       # Chama o teste de Objetivo
       # ----------------------
       teste, chave = Teste_de_Objetrivo_Dfs(tabuleiro, linha, coluna)
       if (teste == True and chave == 3):
           coluna += 1
           caminho.append((linha, coluna))
           final = True
 
       # -----------------------
       # Funções sucessor
       # -----------------------
 
       # Verifica para cima
       if(acesso == 4 and linha > 0 and linha <= 10 and coluna > 0 and coluna <= 10 and tabuleiro[linha - 1][coluna] == 0):
           linha -= 1
           caminho.append((linha, coluna))
           repeticao = 0
 
       # ----------------------
       # Chama o teste de Objetivo
       # ----------------------
       teste, chave = Teste_de_Objetrivo_Dfs(tabuleiro, linha, coluna)
       if (teste == True and chave == 4):
           linha -= 1
           caminho.append((linha, coluna))
           final = True
 
       repeticao += 1
 
   return(caminho, final)
 
 
def interacoes(caminho):
   return len(caminho)
 
 
def Grafico(tabuleiro):
   # Inicializa o jogo
   pygame.init()
 
   # Velocidade da demonstração
   Velocidade = 0.08
 
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
 
   # Limitar os frames para não ir muito rápido
   relogio = pygame.time.Clock()
   nivel = 10
 
   # Cria as variáveis para sair do jogo
   sair = True
   continuar = True
 
   # Jogo em si no laco de repeticao
   while sair:
 
       # Preenche o fundo com a cor escolhida
       tela.fill(BRANCO)
 
       # Limita o frames portanto a velocidade do movimento (fps)
       relogio.tick(nivel)
 
       while continuar:
           # Atualiza a tela
           pygame.display.update()
 
           # Le a tela do display
           for evento in pygame.event.get():
               # Se o usuário clicar no x fechar o display
               if evento.type == pygame.QUIT:
                   caminho = False
           # ----------------------------------------------------------------------------
           # Bloco da parte gráfica inicial
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
           # Bloco da análise e da parte gráfica depois da análise
           # ----------------------------------------------------------------------------
           if(resultado == False):
               # Onde o agente inicializa
               caminho, resultado = Sucessor_Dfs(tabuleiro, 1, 1)
 
           # Imprime toda parte final da análise
           else:
               print("Custo de Etapa Total Busca em Profundidade:", interacoes(caminho))
               # ---------------------------------------------------
               # print(caminho)
               # ---------------------------------------------------
               for i in range(len(caminho)):
                   lin, col = caminho[i]
                   # Le a tela do display
                   for evento in pygame.event.get():
                       # Se o usuário clicar no x fechar o display
                       if evento.type == pygame.QUIT:
                           caminho = False
                           sair = False
 
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
           # Se o usuário clicar no x fechar o display
           if evento.type == pygame.QUIT:
               sair = False
 
   # Fecha o Jogo
   pygame.quit()