# graph: matriz de adjacência
from math import inf


# a conveção adotada nesse exemplo para assinalar vértices não adjacentes é '< 0'
def dijkstra(graph: list, origin: int, destiny: int):
    cost = [inf for _ in graph]
    route = [origin for _ in graph]
    cost[origin] = 0

    opened = [i for i in range(0, len(graph))]
    closed = []

    while len(opened) != 0:
        v = opened[len(opened) - 1]
        for i in opened:
            if cost[i] < cost[v]:
                v = i
        closed.append(v)
        opened.remove(v)

        adj = list(filter(lambda x: graph[v][x] > 0, opened))

        # percorre os vértices abertos, adjacentes ao vértice v, e maiores que 0
        for u in adj:
            if cost[v] + graph[v][u] < cost[u]:
                cost[u] = cost[v] + graph[v][u]
                route[u] = v

    i = destiny
    shortest_route = list()
    while i != origin:
        shortest_route.insert(0, i)
        i = route[i]
    shortest_route.insert(0, origin)

    return shortest_route, cost[destiny]


# por convenção as arestas assinaladas com o valor '-1' são infinitas, ou seja, não existem
def floyd_warshall(graph):
    n = len(graph)
    graph = list(map(lambda lin: list(map(lambda col: inf if col == -1 else col, lin)), graph))

    w = graph
    pre = w.copy()
    for k in range(n):
        for v in range(n):
            for u in range(n):
                w[v][u] = min(pre[v][u], pre[v][k] + pre[k][u])
        pre = w.copy()

    return w


# por convenção as arestas assinaladas com o valor '-1' são infinitas, ou seja, não existem
''' O algoritmo de Bellman-Ford vai iterar n-1 vezes todos os vértices e analisar o seu predecessor.
Caso ainda não foi descoberto, seu custo será INF e não será analisado.
Caso foi descoberto ele vai analisar todos os seus adjacentes e atualizar seus custos e suas rotas se o caminho ao passar por ele for menor'''
def bellman_ford(graph, origin, destiny):
    graph = list(map(lambda lin: list(map(lambda col: inf if col == -1 else col, lin)), graph))
    n = len(graph)

    cost = [inf for _ in graph]
    route = [origin for _ in graph]
    cost[origin] = 0

    for _ in range(n):
        for v in range(n):
            adj = graph[v]

            for u in range(n):
                if cost[v] + graph[v][u] < cost[u] and adj[u] != inf:
                    cost[u] = cost[v] + graph[v][u]
                    route[u] = v

    i = destiny
    shortest_route = list()
    while i != origin:
        shortest_route.insert(0, i)
        i = route[i]
    shortest_route.insert(0, origin)

    return shortest_route, cost[destiny]



bellman_ford([[0,6,-1,7,-1], [-1,0,5,8,-4], [-1,-2,0,-1,-1], [-1,-1,-3, 0,9], [2,-1,7,-1,0]], 0, 4)