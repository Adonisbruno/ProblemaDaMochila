from ProblemaMochila import *
import sys

def main():
    global vetor
    if len(sys.argv) < 2:
        print("python main.py entrada.txt")
        sys.exit(-1)
    try:
        vetor = lerArquivoToList(sys.argv[1])
    except ValueError:
        print("valores invalidos")
        sys.exit(-1)

if __name__ == "__main__":
    main()
    
    # extrai as dimensoes da matriz, remove ela da lista e retorna a lista tambem
    lista, linhas, capacidade = extrairDimensoesMatriz(vetor)
    # extraindo peso, valor e inicializando matriz da Mochila com zeros
    matriz, peso, valor = extrairPesoValor(lista, linhas, capacidade)
    # calculando valores da matriz da Mochila
    matrizMochila = gerarMatrizMochila(matriz, peso, valor)
    # obtendo os itens que vao na mochila e seu valor total
    mochila, valorTotal = obterItensMochila(matrizMochila, peso)
    # saida de interesse
    print('Seus pesos: ', mochila)
    print('Itens que vao na mochila')
    print('Com peso total de', sum(mochila))
    print('Com valor total de', valorTotal)