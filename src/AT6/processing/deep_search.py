def deep_search(seq, g, v):
    seq.append(v)
    for i in g[v]:
        if i not in seq:
            seq = deep_search(seq, g, i)

    return seq


def dfs_recursive(g: dict, v: int) -> list:
    sequencia = []
    deep_search(sequencia, g, v)
    return sequencia


def dfs(g: dict, v: int) -> list:
    sequencia = [] # sequencia de vértices visitados
    nao_visitado = list(g.keys())
    i = v

    # percorre todos os elementos da lista 'nao_visitado'
    while len(nao_visitado) != 1:
        # adiciona o elemento em questão na lista 'sequencia'
        sequencia.append(i)
        nao_visitado.remove(i)

        backtrack = True
        for j in nao_visitado:
            if j in g.get(i):
                i = j
                backtrack = False
                break
        # se não há nenhum vértice inédito o algoritmo faz o backtrack e volta ao elemento não visitado
        if backtrack:
            i = nao_visitado[0]

    sequencia.append(nao_visitado[0])

    return sequencia


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
