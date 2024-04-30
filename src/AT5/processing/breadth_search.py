def bfs(G: dict, v: int):
    vert_analisados = dict()
    for i in G.keys():
        vert_analisados[i] = False
    q = []
    sequencia = []
    q.append(v)

    while len(q) != 0:
        v = q.pop(0)
        for adj in G.get(v):
            if adj not in q and adj not in sequencia and adj != v:
                q.append(adj)

        sequencia.append(v)
        vert_analisados[v] = True

        if len(sequencia) != len(G.keys()) and len(q) == 0:
            for vert in vert_analisados.keys():
                if not vert_analisados[vert]:
                    q.append(vert)
                    break

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
