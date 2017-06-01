from collections import defaultdict

def bfs_find(u, v, graph):
    visitados = defaultdict(int)      
    visitados[u] = 1
    prox = [u]
    while len(prox) != 0:
        level = []
        for node in prox:
            for vizinho, gasto in graph[node]:
                if vizinho == v:
                    return True
                if not visitados[vizinho]:
                    prox.append(vizinho)
                    level.append(vizinho)
                    visitados[vizinho] = 1
        prox = level
        
    return False
                                
def existe_mao_dupla(u, v, graph):
    return bfs_find(v, u, graph.copy()) and bfs_find(u, v, graph.copy())
    
                            
while True:
    n, e = map(int, input().split())
    
    if n == 0 and e == 0:
        break

    graph = defaultdict(set)

    for _ in range(e):

        x, y, h = map(int, input().split())
        graph[x].add((y,h))

    k = int(input())
    print (graph)

    paises = defaultdict(set)

    # grafo dos pais, cada componente conexo eh um pais
    for pais_a, s in graph.items():
        for t in s:
            pais_b = t[0]
            ret = existe_mao_dupla(pais_a, pais_b, graph)
            if ret:
                 paises[pais_a].add(pais_b)
                 paises[pais_b].add(pais_a)

    print ("paises: ", paises)
          
    for _ in range(k):
        # dijkstra
        # se agencia no mesmo pais entao gasto eh 0
        u, v = map(int, input().split())
        
