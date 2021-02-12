#------------------------------- /usr/bin/g++-7 ------------------------------#
#------------------------------- coding: utf-8 -------------------------------#
# Criado por:   Jean Marcelo Mira Junior
#               Victor Philos Donato Luiz da Silva
# Versão: 1.0
# Criado em: 11/02/2021
# Sistema operacional: Linux - Ubuntu 20.04.1 LTS

#------------------------------ Pacotes --------------------------------------#
import biblioteca as bib
import numpy as np


#-----------------------------------------------------------------------------#
# Tabuleiro para analise
#                          0  1  2  3  4  5  6  7  8  9
tabuleiro1 = np.array([[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],                   # Borda
                       [5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],                   # 0
                       [5, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],                   # 1
                       [5, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],                   # 2
                       [5, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 5],                   # 3
                       [5, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 5],                   # 4
                       [5, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 5],                   # 5
                       [5, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 5],                   # 6
                       [5, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 5],                   # 7
                       [5, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 5],                   # 8
                       [5, 1, 1, 0, 3, 0, 0, 0, 0, 1, 1, 5],                   # 9
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]], dtype=np.int)    # Borda

# Tabuleiro para analise
#                          0  1  2  3  4  5  6  7  8  9
tabuleiro2 = np.array([[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],                   # Borda
                       [5, 2, 0, 0, 0, 0, 1, 1, 1, 1, 1, 5],                   # 0
                       [5, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 5],                   # 1
                       [5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],                   # 2
                       [5, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 5],                   # 3
                       [5, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 5],                   # 4
                       [5, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 5],                   # 5
                       [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 5],                   # 6
                       [5, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5],                   # 7
                       [5, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 5],                   # 8
                       [5, 0, 1, 1, 0, 3, 1, 1, 1, 1, 1, 5],                   # 9
                       [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]], dtype=np.int)    # Borda


# Tabuleiro para analise
#                       0  1  2  3  4  5  6  7  8  9
tabuleiro3 = np.array([[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   # 0
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   # 1
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   # 2
                       [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],                   # 3
                       [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],                   # 4
                       [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],                   # 5
                       [0, 0, 1, 1, 1, 1, 0, 1, 0, 0],                   # 6
                       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],                   # 7
                       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],                   # 8
                       [0, 0, 1, 3, 1, 1, 1, 1, 0, 0], ], dtype=np.int)  # 9

# Tabuleiro para analise
#                       0  1  2  3  4  5  6  7  8  9
tabuleiro4 = np.array([[2, 1, 1, 1, 1, 0, 0, 0, 0, 0],                   # 0
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],                   # 1
                       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],                   # 2
                       [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],                   # 3
                       [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],                   # 4
                       [0, 1, 1, 1, 1, 0, 0, 1, 1, 1],                   # 5
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],                   # 6
                       [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],                   # 7
                       [1, 0, 0, 1, 0, 0, 1, 1, 1, 1],                   # 8
                       [1, 0, 1, 1, 3, 0, 0, 0, 0, 0]], dtype=np.int)    # 9

bib.Grafico(tabuleiro2)
