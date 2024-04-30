import os
import sys
import time

from processing.deep_search import *

INSTANCES_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'files/instances')) + '/'


def main(instance):
    relative = INSTANCES_PATH + instance + '.txt'
    matriz = list()

    with open(relative, "r") as file:
        for line in file:
            matriz.append([int(i) for i in line.strip().split(" ")])

    listAdj = criaListaAdjacencias(matriz)

    begin = time.time()
    print(dfs_recursive(listAdj, 0))
    end = time.time()
    print(f'tempo de execução (deep first search recursive): {end - begin}')

    begin = time.time()
    print(dfs(listAdj, 0))
    end = time.time()
    print(f'tempo de execução (deep first search): {end - begin}')

if __name__ == '__main__':
    main(sys.argv[1])
