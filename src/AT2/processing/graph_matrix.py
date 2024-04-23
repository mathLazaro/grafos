import numpy as np


# Retorna o tipo do grafo representado por uma dada matriz de adjacências
def tipoGrafo(matriz):
    len_matriz = len(matriz)
    tipo = 0

    # verifica se é um digrafo
    for i in range(len_matriz):
        # quebra o laço caso for um digrafo
        if tipo == 1:
            break
        for j in range(i, len_matriz):
            if matriz[i][j] != matriz[j][i]:
                tipo = 1
                break

    # verfica se é um multigrafo
    for i in range(len_matriz):
        # quebra o laço caso for um multigrafo
        if tipo >= 20:
            break

        for j in range(i + 1, len_matriz):
            if matriz[i][j] > 1 or matriz[j][i] > 1:
                tipo = 20 if tipo % 2 == 0 else 21
                break

    # verifica a diagonal para definir se é pseudografo
    for i in np.diagonal(matriz):
        if i > 0:
            tipo = 30 if tipo % 2 == 0 else 31
            break

    return tipo


# Verifica se os vértices vi e vj são adjacentes.
def verificaAdjacencia(matriz, vi, vj):
    a1 = bool(matriz[vi][vj])
    a2 = bool(matriz[vj][vi])

    # retorna True para vértices adjacentes (!= 0)
    #         False para vértices não adjacentes (==0)
    return a1 or a2


# Retorna o valor da densidade do grafo.
def calcDensidade(matriz):
    tipo = tipoGrafo(matriz) % 2
    densidade = 0
    arestas = 0
    vertices = 0

    # Calcula a quantidade de vértices e arestas
    for i in range(0, len(matriz)):
        # verifica se o vértice foi removido
        if matriz[i][0] == -1:
            continue
        vertices += 1
        for j in range(i, len(matriz)):
            # verifica se algum dos vértices analisados foi removido
            if matriz[i][j] < 0:
                continue
            # grafo simples
            if tipo == 0:
                arestas += matriz[i][j]
                continue
            # digrafo
            arestas += matriz[i][j] + matriz[j][i] if i != j else matriz[i][j]

    # calcula a densidade de acordo com o tipo do grafo
    if vertices > 0:
        densidade = arestas / (vertices * (vertices - 1))
        densidade *= 2 if tipo == 0 else 1

    return round(densidade, 3)


# Insere uma aresta no grafo considerando o par de vértices vi e vj.
def insereAresta(matriz, vi, vj):
    tipo = tipoGrafo(matriz) % 2
    ultimo_vertice = len(matriz) - 1

    # verifica se os vértices fornecidos são válidos
    if vi < 0 or vj < 0 or vi > ultimo_vertice or vj > ultimo_vertice:
        return np.array(matriz, dtype=int)

    if matriz[vi][vj] < 0 or matriz[vj][vi] < 0:
        return np.array(matriz, dtype=int)

    matriz[vi][vj] += 1
    if tipo == 0:
        matriz[vj][vi] += 1

    return np.array(matriz, dtype=int)


# Insere um vértice no grafo.
def insereVertice(matriz):
    # adiciona uma coluna em cada linha
    for i in matriz:
        i.append(0)

    # adiciona uma linha
    matriz.append([0] * (len(matriz) + 1))

    return np.array(matriz, dtype=int)


# Remove uma aresta do grafo considerando o par de vértices vi e vj.
def removeAresta(matriz, vi, vj):
    tipo = tipoGrafo(matriz) % 2
    ultimo_vertice = len(matriz) - 1

    # verifica se os vértices fornecidos são válidos
    if vi < 0 or vj < 0 or vi > ultimo_vertice or vj > ultimo_vertice:
        return np.array(matriz, dtype=int)

    if matriz[vi][vj] < 0 or matriz[vj][vi] < 0:
        return np.array(matriz, dtype=int)

    matriz[vi][vj] -= 1
    if tipo == 0:
        matriz[vj][vi] -= 1

    return np.array(matriz, dtype=int)


# Remove um vértice do grafo.
def removeVertice(matriz, vi):
    # percorre a linha e a coluna do vértice a ser removido
    for i in range(len(matriz)):
        matriz[vi][i] = -1
        matriz[i][vi] = -1

    return np.array(matriz, dtype=int)

