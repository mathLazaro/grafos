import sys

from src.graph_paths import *


def main(instance):
    PATH = 'instances/' + instance + '.txt'
    matriz = list()

    with open(PATH, "r") as file:
        for line in file:
            matriz.append([int(i) for i in line.strip().split(" ")])

    print(f'Matriz de alcançabilidade: {warshall(matriz)}')
    print()

    print(f'Grafo euleriano: {caminhoEuleriano(matriz)}')


if __name__ == '__main__':
    main(sys.argv[1])
