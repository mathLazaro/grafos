from math import inf
from functools import cmp_to_key


def prim(graph: list, i=0):
    length = len(graph)
    selected = [i]

    not_selected = [k for k in range(length)]
    not_selected.remove(i)

    cost = 0

    res = []

    while len(res) < length - 1:
        minimal_edge = (0, 0)
        weight = inf

        for v in selected:
            for u in range(length):
                aux_weight = graph[v][u]
                if u in not_selected and aux_weight > 0 and aux_weight < weight:
                    minimal_edge = (v, u)
                    weight = aux_weight

        cost += weight
        not_selected.remove(minimal_edge[1])
        selected.append(minimal_edge[1])

        res.append(minimal_edge)

    return res, cost


# ordena as arestas de acordo com o peso
def get_edges(graph: list):
    res = dict()
    for v in range(len(graph)):
        for u in range(len(graph)):
            if graph[v][u] != 0:
                if v > u:
                    res[(u, v)] = graph[v][u]
                    continue
                res[(v, u)] = graph[v][u]
    return sorted(res.keys(), key=cmp_to_key(lambda e1, e2: res[e1] - res[e2]))


# para verificar um ciclo pelo menos uma das extremidades deve ser não descoberta
def kruskal(graph, i=0):
    edges = get_edges(graph)  # arestas ordenadas por peso
    components = []
    res = []
    cost = 0

    while len(res) < len(graph) - 1:
        for e in edges:
            v = e[0]
            u = e[1]

            component_v = None
            component_u = None

            for c in components:
                if component_v is None and v in c:
                    component_v = c
                if component_u is None and u in c:
                    component_u = c

            if component_v is not None and component_u is not None:
                if component_v is component_u:
                    continue
                else:
                    components.append(component_v + component_u)
                    components.remove(component_u)
                    components.remove(component_v)
            else:
                if component_v is None and component_u is None:
                    components.append([v, u])
                elif component_v is None:
                    component_u.append(v)
                elif component_u is None:
                    component_v.append(u)

            res.append(e)
            cost += graph[v][u]

    return res, cost


l = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
     [4, 0, 8, 0, 0, 0, 0, 11, 0],
     [0, 8, 0, 7, 0, 4, 0, 0, 2],
     [0, 0, 7, 0, 9, 14, 0, 0, 0],
     [0, 0, 0, 9, 0, 10, 0, 0, 0],
     [0, 0, 4, 14, 10, 0, 2, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 1, 6],
     [8, 11, 0, 0, 0, 0, 1, 0, 7],
     [0, 0, 2, 0, 0, 0, 6, 7, 0]]
# # expected: {0, 1}, {0, 7}, {7, 6}, {6, 5}, {5, 2}, {2, 8}, {2, 3}, {3, 4}, 37

print(prim(l))
print(kruskal(l))
