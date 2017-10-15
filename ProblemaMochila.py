import numpy as np

def lerArquivoToList(file):
    # file := local e nome do arquivo "../xp.txt"
    arr = []
    inp = open(file, "r")
    # ler a linha do arquivo
    for line in inp.readlines():
        # adiciona uma sublista a lista
        arr.append([])
        # separa os elementos nos espacos, a cada espaco, separa...
        for i in line.split():
            # converte para inteiro e adiciona ao final da linha
            arr[-1].append(int(i))
    return arr

def extrairDimensoesMatriz(lista):
    # parametros := saida de lerArquivoToList
    linhas, capacidade = lista[0][0], lista[0][1]
    del lista[0]
    return lista, linhas, capacidade

def extrairPesoValor(lista, linhas, capacidade):
    # parametros := saida de extrairDimensoesMatriz(,)
    m = np.zeros((linhas + 1, capacidade + 1), dtype=int)
    p = np.zeros((linhas, 1), dtype=int)
    v = np.zeros((linhas, 1), dtype=int)
    for i in range(len(lista)):
        p[i], v[i] = lista[i]
    return m, p, v

def gerarMatrizMochila(matriz, peso, valor):
    # parametros := saidas de extrairPesoValor(,,)
    for p in range(1, matriz.shape[0]):
        for c in range(1, matriz.shape[1]):
            # print(p,c)
            tmpPeso = peso[p - 1]
            if tmpPeso <= c:
                # print(p,c,tmpPeso)
                tmpValor = valor[p - 1]
                tmpValorAnteior = matriz[p - 1][c - peso[p - 1]]
                matriz[p, c] = tmpValor + tmpValorAnteior
            else:
                if matriz[p - 1][c] > matriz[p, c]:
                    matriz[p, c] = matriz[p - 1][c]
                else:
                    matriz[p, c] = 0
    return matriz

def obterItensMochila(matriz, peso):
    mochila = []
    # pegando dimensoes da matriz
    p = matriz.shape[0] - 1  # pesos
    c = matriz.shape[1] - 1  # capacidades
    valorTotal = matriz[p][c]  # valor total levado
    tmpCapacidade = c

    while p > 0:
        if matriz[p][tmpCapacidade] != matriz[p - 1][tmpCapacidade]:
            # print(matriz[p][tmpCapacidade], matriz[p-1][tmpCapacidade])
            tmpCapacidade = tmpCapacidade - peso[p - 1]
            mochila.append(int(peso[p - 1]))
            p -= 1
        else:
            p -= 1
    return mochila, valorTotal