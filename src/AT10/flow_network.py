import math


def _procedure_dfs(sequence: list, graph: list, v: int) -> list:
    sequence.append(v)
    for u in range(len(graph)):
        if graph[v][u] > 0 and u not in sequence:
            _procedure_dfs(sequence, graph, u)
    return sequence


def dfs(graph: list, source: int, sink: int) -> list:
    search = _procedure_dfs([], graph, source)

    if sink not in search:
        return []

    while search[-1] != sink:
        search.pop()

    sequence = [sink]
    for i in range(len(search) - 1, 0, -1):
        v = search[i]
        u = sequence[0]
        if graph[v][u] > 0:
            sequence.insert(0, v)
    sequence.insert(0, source)

    return sequence


def find_throat(graph: list, path: list) -> int:
    throat = math.inf
    for i in range(len(path) - 1):
        throat = min(throat, graph[path[i]][path[i + 1]])
    return throat


def flow_network(graph: list, source: int, sink: int) -> int:
    max_flow = 0
    while True:
        path = dfs(graph, source, sink)
        if len(path) == 0:
            break
        throat = find_throat(graph, path)
        for i in range(len(path) - 1):
            v = path[i]
            u = path[i + 1]
            graph[v][u] -= throat
            graph[u][v] += throat
        max_flow += throat
    return max_flow


l = [[0, 7, 0, 4, 0, 0],
     [0, 0, 5, 0, 3, 0],
     [0, 0, 0, 0, 0, 8],
     [0, 3, 0, 0, 2, 0],
     [0, 0, 3, 0, 0, 5],
     [0, 0, 0, 0, 0, 0]]
# expected 10

l1 = [[0, 5, 0, 4, 0, 0],
      [0, 0, 6, 0, 0, 0],
      [0, 0, 0, 0, 8, 5],
      [0, 3, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 2],
      [0, 0, 0, 0, 0, 0]]

print(flow_network(l, 0, 5))
print(flow_network(l1, 0, 5))
