import sys

import numpy as np

import processing.graph_list as gf
from data_inout.output_result import *
from data_inout.read_instance import *


def menu() -> int:
    print('1 - tipo grafo')
    print('2 - verificar adjacência')
    print('3 - calcular densidade')
    print('4 - inserir aresta')
    print('5 - inserir vértice')
    print('6 - remover aresta')
    print('7 - remover vértice')
    print('0 - sair')
    return int(input('Opção: '))


def main(instance: str):
    # leitura do arquivo em multi list
    matriz = read_instance(instance)

    # cria uma lista de adjacência
    listaAdj = gf.criaListaAdjacencias(matriz)

    # printa a instância para melhor vizualização
    write_result('------\ninstância: ' + instance)
    write_result(str(np.array(matriz, dtype=int)))

    while True:
        op = menu()
        result = ''
        if op == 0:
            break
        elif op == 1:
            result = 'tipo do grafo: ' + str(gf.tipoGrafo(listaAdj))
        elif op == 2:
            v1, v2 = int(input('v1: ')), int(input('v2: '))
            result = f'{v1} e {v2} adjacentes: {gf.verificaAdjacencia(listaAdj, v1, v2)}'
        elif op == 3:
            result = 'densidade: ' + str(gf.calcDensidade(listaAdj))
        elif op == 4:
            v1, v2 = int(input('v1: ')), int(input('v2: '))
            result = str(gf.insereAresta(listaAdj, v1, v2))
        elif op == 5:
            result = str(gf.insereVertice(listaAdj))
        elif op == 6:
            v1, v2 = int(input('v1: ')), int(input('v2: '))
            result = str(gf.removeAresta(listaAdj, v1, v2))
        elif op == 7:
            v1 = int(input('v1: '))
            result = str(gf.removeVertice(listaAdj, v1))
        write_result(result)

    write_result('fim da instância')


if __name__ == '__main__':
    main(sys.argv[1])
