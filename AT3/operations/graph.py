# recebe um array lido do dataset e retorna uma lista de ajacencias (dict)
def criaListaAdjacencias(matriz: list) -> dict:
    # key: índice (int)
    # value: índice dos vértices adjacentes ao indice-key (list)
    listAdj = dict()
    lenght = len(matriz)

    # percorre a matriz
    for vi in range(0, lenght):
        adj = []
        for vj in range(0, lenght):
            # adiciona as arestas à lista 'adj'
            for k in range(0, matriz[vi][vj]):
                adj.append(vj)
        listAdj[vi] = adj

    return listAdj


# retorna o tipo do grafo
def tipoGrafo(listaAdj: dict) -> int:
    ''' 0 - simples, 1 - digrafo,
    20 - multigrafo simples, 21 - multigrafo dirigido,
    30 - pseudo simples, 31 - pseudo dirigido'''
    tipo = 0

    # analisa se é um grafo dirigido
    for vi in range(0, len(listaAdj)):
        if tipo == 1:
            break
        adj = listaAdj.get(vi)
        for vj in adj:
            if vi not in listaAdj.get(vj):
                tipo = 1
                break

    # analisa se é um multigrafo
    for vi in range(0, len(listaAdj)):
        temp = set()
        if tipo >= 20:
            break
        adj = listaAdj.get(vi)
        for vj in adj:
            # verfica se o vértice já foi adicionado no set 'temp'
            if vj not in temp:
                temp.add(vj)
            # se já foi adicionado significa que há mais de uma adjacencia pra os mesmos vértices
            else:
                # portanto é um multigrafo
                tipo = 20 if tipo % 2 == 0 else 21
                break

    # analisa se é um pseudografo
    for vi in range(0, len(listaAdj)):
        if vi in listaAdj.get(vi):
            tipo = 30 if tipo % 2 == 0 else 31
            break

    return tipo


# verifica se existe aresta entre v1 e v2
def verificaAdjacencia(listaAdj: dict, vi: int, vj: int) -> bool:
    return vi in listaAdj[vj] or vj in listaAdj[vi]


# retorna o valor da densidade do grafo.
def calcDensidade(listaAdj: dict) -> float:
    # 0 - simples
    # 1 - dirigido
    tipo = tipoGrafo(listaAdj) % 2

    lacos = 0
    qtd_adj = 0

    for vi, adj in listaAdj.items():
        qtd_adj += len(adj)
        if vi in adj:
            lacos += 1

    vertices = len(listaAdj)
    if tipo == 0:
        arestas = qtd_adj / 2 + lacos
    else:
        arestas = qtd_adj

    densidade = arestas / (vertices * (vertices - 1)) if vertices > 1 else 0
    if tipo == 0:
        densidade *= 2

    return round(densidade, 3)


# insere uma aresta no grafo considerando o par de vértices vi e vj.
def insereAresta(listaAdj: dict, vi: int, vj: int) -> dict:
    tipo = tipoGrafo(listaAdj) % 2

    # grafo simples
    if tipo == 0:
        listaAdj.get(vi).append(vj)
        listaAdj.get(vj).append(vi)
    # digrafo
    else:
        listaAdj.get(vi).append(vj)

    listaAdj.get(vi).sort()
    return listaAdj


# insere um vértice no grafo.
def insereVertice(listaAdj: dict, vi: int) -> dict:
    listaAdj[vi] = list()
    return listaAdj


# remove uma aresta do grafo considerando o par de vértices vi e vj.
def removeAresta(listaAdj: dict, vi: int, vj: int) -> dict:
    tipo = tipoGrafo(listaAdj) % 2

    # caso simples
    if tipo == 0:
        listaAdj.get(vi).remove(vj)
        listaAdj.get(vj).remove(vi)
    # caso dirigido
    else:
        listaAdj.get(vi).remove(vj)

    return listaAdj


# remove um vértice do grafo.
def removeVertice(listaAdj: dict, vi: int) -> dict:
    listaAdj.pop(vi)
    for row in listaAdj.values():
        while vi in row:
            row.remove(vi)
    return listaAdj
