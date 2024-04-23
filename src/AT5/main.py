import os
import sys

from processing.breadth_search import *

INSTANCES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'files/instances')) + '/'


def main(instance):
    relative = INSTANCES_PATH + instance + '.txt'
    matriz = list()

    with open(relative, "r") as file:
        for line in file:
            matriz.append([int(i) for i in line.strip().split(" ")])

    print(f'Sequência de busca: {bfs(criaListaAdjacencias(matriz), 0)}')


if __name__ == '__main__':
    main(sys.argv[1])
