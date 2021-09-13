import numpy as np
import matplotlib.pyplot as plt
import random


# Função que exibe o ambiente na tela
def exibir(I):
    global posAPAx
    global posAPAy

    # Altera o esquema de cores do ambiente
    plt.imshow(I, 'gray')
    plt.nipy_spectral()

    # Coloca o agente no ambiente
    plt.plot([posAPAy], [posAPAx], marker='o', color='r', ls='')

    plt.show(block=False)

    # Pausa a execução do código por 0.5 segundos para facilitar a visualização
    plt.pause(10000000000.5)
    plt.clf()



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