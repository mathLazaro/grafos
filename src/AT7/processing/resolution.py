def classificaArestas(graph: dict, v: int):
    gray = [v]
    white = list(graph.keys())
    black = []
    counter = 2
    timeDF = dict([i, [0, 0]] for i in white)
    aux_graph = graph.copy()
    white.remove(v)
    timeDF[v][0] = 1

    while len(black) != len(graph):
        origin = gray[len(gray) - 1]
        try:
            destiny = aux_graph.get(origin).pop(0)  # pode dar erro em caso de backtrack

            # analisa a aresta do menor número adjacente
            # caso tree
            if destiny in white:
                print(f'{origin} {destiny} Tree')
                # muda a cor do destino
                white.remove(destiny)
                gray.append(destiny)
                # atualiza o tempo de descoberta da origem
                timeDF[destiny][0] = counter
                counter += 1
            # caso back
            elif destiny in gray or destiny == origin:
                print(f'{origin} {destiny} Back')

            else:
                # caso forward
                if timeDF[origin][0] < timeDF[destiny][0]:
                    print(f'{origin} {destiny} Forward')

                # caso cross
                else:
                    print(f'{origin} {destiny} Cross')

        except:
            # muda a cor do vertice analisado(origin) para preto
            black.append(origin)
            gray.remove(origin)

            # atualiza o tempo de finalização
            timeDF[origin][1] = counter
            counter += 1

        # caso exista alguma parte desconexa ou ainda não descoberta
        if len(gray) == 0 and len(black) != len(graph):
            # adiciona na pilha(cinza)
            new = white.pop(0)
            gray.append(new)

            # atualiza o tempo de descoberta
            timeDF[new][0] = counter  # possivelmente erro
            counter += 1

    return timeDF


def temposVertices(graph, v):
    d = classificaArestas(graph, v)
    return dict([i, str(d.get(i)[0]) + '/' + str(d.get(i)[1])] for i in d)


def verificaDAG(graph: dict):
    v = 0
    gray = [v]
    white = list(graph.keys())
    black = []
    counter = 2
    timeDF = dict([i, [0, 0]] for i in white)
    aux_graph = graph.copy()
    white.remove(v)
    timeDF[v][0] = 1

    while len(black) != len(graph):
        origin = gray[len(gray) - 1]
        try:
            destiny = aux_graph.get(origin).pop(0)  # pode dar erro em caso de backtrack

            # analisa a aresta do menor número adjacente
            # caso tree
            if destiny in white:
                # muda a cor do destino
                white.remove(destiny)
                gray.append(destiny)
                # atualiza o tempo de descoberta da origem
                timeDF[destiny][0] = counter
                counter += 1
            # caso back
            elif destiny in gray or destiny == origin:
                return 'NÃO DAG'

        except:
            # muda a cor do vertice analisado(origin) para preto
            black.append(origin)
            gray.remove(origin)

            # atualiza o tempo de finalização
            timeDF[origin][1] = counter
            counter += 1

        # caso exista alguma parte desconexa ou ainda não descoberta
        if len(gray) == 0 and len(black) != len(graph):
            # adiciona na pilha(cinza)
            new = white.pop(0)
            gray.append(new)

            # atualiza o tempo de descoberta
            timeDF[new][0] = counter  # possivelmente erro
            counter += 1

    print('DAG')


if __name__ == '__main__':
    d = {0: [1, 3], 1: [4], 2: [4, 5], 3: [], 4: [3], 5: []}
    print(verificaDAG(d))
