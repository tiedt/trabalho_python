import numpy as np
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import random
import sys

PosicaoX = 1
PosicaoY = 1
TamanhoMatriz = 6
ContadorPontos = 0


x = np.arange(1,TamanhoMatriz,1)
x1 = np.sin(1 * x)




p2 = np.arange(0,2,1)
p3 = np.arange(TamanhoMatriz -1, TamanhoMatriz + 1, 1)
p4 = np.arange(1,TamanhoMatriz, 1)
x2 = np.sin(1 * p4)

# Função que exibe o ambiente na tela
def exibir():

        ##figura,z = plt.subplots(subplot_kw={'xlim': [0,TamanhoMatriz], 'ylim': [0,TamanhoMatriz]}, clear=True)
        #plt.imshow(I, 'gray')
        plt.nipy_spectral()
        figura,z = plt.plot([0,TamanhoMatriz], [0,TamanhoMatriz], marker='o', color='r', ls='')
        criarMeio(z)
        criarParedeLinha(0.5,0.5,z)
        criarParedeColuna(0.5,0.5,z)
        plt.pause(0.5)
        plt.clf()


def criarMeio(z):
    collection = collections.BrokenBarHCollection.span_where(x,ymin=1,ymax=TamanhoMatriz-1,where=x1< TamanhoMatriz - 1, facecolor='green', alpha=0.5)
    z.add_collection(collection)


def criarParedeColuna(x,y,z):
    plt.plot(x,y,'--.y',markersize=40)
    plt.plot(x + TamanhoMatriz - 1, y, '--.y', markersize=40)
    if y < TamanhoMatriz - 2:
        y+=1
        criarParedeColuna(x,y,z)
    else:
        collection = collections.BrokenBarHCollection.span_where(p2,ymin=1,ymax=TamanhoMatriz-1,where=x2< TamanhoMatriz - 1, facecolor='blue', alpha=0.5)
        z.add_collection(collection)
        collection = collections.BrokenBarHCollection.span_where(p3,ymin=1,ymax=TamanhoMatriz-1,where=x2< TamanhoMatriz - 1, facecolor='blue', alpha=0.5)
        z.add_collection(collection)

def criarParedeLinha(x,y,z):
    plt.plot(x,y,'--.y',markersize=40)
    plt.plot(x,y + (TamanhoMatriz -1), '--.y',markersize=40)
    if x < TamanhoMatriz - 1:
        x+=1
        criarParedeLinha(x,y,z)
    else:
        collection = collections.BrokenBarHCollection.span_where(p4,ymin=TamanhoMatriz-1,ymax=TamanhoMatriz,where=x2< TamanhoMatriz, facecolor='blue', alpha=0.5)
        z.add_collection(collection)
        collection = collections.BrokenBarHCollection.span_where(p4,ymin=0,ymax=1,where=x2< TamanhoMatriz, facecolor='blue', alpha=0.5)
        z.add_collection(collection)


exibir()