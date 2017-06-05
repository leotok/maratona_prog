# https://www.urionlinejudge.com.br/judge/pt/problems/view/1148
# http://www.gilles-bertrand.com/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html

from collections import defaultdict

def bfs_find(u, v, graph):
    visitados = defaultdict(int)   
    visitados[u] = 1
    prox = [u]
    while len(prox) != 0:
        level = []
        for node in prox:
            for vizinho in graph[node]:
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
    
def dijkstra(graph,src,dest,paises,visited=None,distances=None,predecessors=None):

    if visited is None:
        visited = []
    if distances is None:
        distances = defaultdict(lambda: float('inf'))
    if predecessors is None:
        predecessors = {}

     # a few sanity checks
    if src not in graph:
        return float('inf')
    if dest not in graph:
        return float('inf')
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        return distances[dest]
    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                if mesmo_pais(src, neighbor, paises):
                    new_distance = distances[src]
                else:
                    new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        return dijkstra(graph,x,dest,paises,visited,distances,predecessors)

def mesmo_pais(u, v, paises):
    if v in paises[u] and u in paises[v]:
        return True
    else:
        return False

if __name__ == '__main__':

    while True:
        n, e = map(int, raw_input().split())
        
        if n == 0 and e == 0:
            break

        graph = defaultdict(dict)

        for _ in xrange(e):

            x, y, h = map(int, raw_input().split())
            graph[x][y] = h

        k = int(raw_input())
        paises = defaultdict(set)

        # grafo dos pais, cada componente conexo eh um pais
        for pais_a, d in graph.items():
            for pais_b, valor in d.items():
                ret = existe_mao_dupla(pais_a, pais_b, graph)
                if ret:
                    paises[pais_a].add(pais_b)
                    paises[pais_b].add(pais_a)

        for _ in xrange(k):
            # dijkstra
            # se agencia no mesmo pais entao gasto eh 0
            u, v = map(int, raw_input().split())
            ret = dijkstra(graph, u, v, paises)
            if ret != float('inf'):
                print ret
            else:
                print "Nao e possivel entregar a carta"
        print
