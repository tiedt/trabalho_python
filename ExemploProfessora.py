import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as collections
from random import randint
import sys

TamanhoMatriz = 6
MatrixSujeira = []
MaximoSujeira = 7

# Função que exibe o ambiente na tela
def exibir(I):
    global posAPAx
    global posAPAy

    # Altera o esquema de cores do ambiente
    plt.imshow(I, 'gray')
    plt.nipy_spectral()
    criarSujeira(MaximoSujeira, MatrixSujeira)
    # Coloca o agente no ambiente
    plt.plot([posAPAy], [posAPAx], marker='o', color='r', ls='')
    disporSujeira(posAPAx,posAPAy)
    plt.show(block=False)

    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(10000000000.5)
    plt.clf()

def criarSujeira(MaximoSujeira, MatrixSujeira):
    x = MatrixSujeira
    if MaximoSujeira < 1:
        return

    CoordenadaSujeiraX = randint(2, TamanhoMatriz - 1)
    CoordenadaSujeiraY = randint(2, TamanhoMatriz - 1)
    CoordenadaSujeiraX = CoordenadaSujeiraX - 1
    CoordenadaSujeiraY = CoordenadaSujeiraY - 1
    coordenadas = [CoordenadaSujeiraX, CoordenadaSujeiraY]

    if coordenadas in MatrixSujeira:
        criarSujeira(MaximoSujeira, x)
    else:
        if CoordenadaSujeiraX == posAPAx and CoordenadaSujeiraY == posAPAy:
            criarSujeira(MaximoSujeira, x)
        else:
            MatrixSujeira.append(coordenadas)
            MaximoSujeira = MaximoSujeira - 1
            criarSujeira(MaximoSujeira, x)


def disporSujeira(posAPAx,posAPAy):
    k = 0
    for i in MatrixSujeira:
        TempX = ''
        TempY = ''
        for j in MatrixSujeira[k]:
            if (TempX == ''):
                TempX = j
            else:
                TempY = j
                plt.plot(float(TempX), float(TempY), 'ow', markersize=10)
                k += 1



    # Matriz que contém o ambiente inicial
    # 1 = parede
    # 0 = limpo
    # 2 = sujo
matriz = [[1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1]]

posAPAx = 1
posAPAy = 1


exibir(matriz)