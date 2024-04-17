import numpy as np


# define uma matriz de alcançabilidade com base no algoritmo de Warshall
# k -> representa o vértice observado
# i -> representa o vértice que será comparado com o vertice k,
#      sendo que a aresta m[i][k] representa as arestas de chegada a k
# j -> representa o vértice com o qual o vértice k será comparado,
#      sendo que a aresta m[k][j] representa as arestas de saída de k
def warshall(matriz: list) -> np.ndarray:
    n = len(matriz)
    mat = np.array(matriz, dtype=int)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 1 or (mat[i][k] == 1 and mat[k][j] == 1):
                    mat[i][j] = 1
                else:

                    mat[i][j] = mat[i][j]
        if k == 1:
            break

    return mat


# Define se o grafo fornecido é euleriano
def caminhoEuleriano(matriz) -> bool:
    n = len(matriz)
    total_impar = 0
    i = 0

    # TODO: o grafo deve ser identificado como conexo para ser euleriano

    while total_impar <= 2 and i < n:
        grau = sum(matriz[i])
        if grau % 2 != 0:
            total_impar += 1
        i += 1

    if total_impar == 2 or total_impar == 0:
        return True
    else:
        return False
