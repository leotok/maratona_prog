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
    
def dijkstra(graph,src,dest,visited=None,distances=None,predecessors=None):

    if visited is None:
        visited = []
    if distances is None:
        distances = {}
    if predecessors is None:
        predecessors = {}

     # a few sanity checks
    if src not in graph:
        raise TypeError('The root of the shortest path tree cannot be found')
    if dest not in graph:
        raise TypeError('The target of the shortest path cannot be found')    
    # ending condition
    if src == dest:
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('shortest path: '+str(path)+" cost="+str(distances[dest])) 
    else :     
        # if it is the initial  run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
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
        dijkstra(graph,x,dest,visited,distances,predecessors)


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
        print (graph)

        paises = defaultdict(set)

        # grafo dos pais, cada componente conexo eh um pais
        for pais_a, d in graph.items():
            for pais_b, valor in d.items():
                ret = existe_mao_dupla(pais_a, pais_b, graph)
                if ret:
                     paises[pais_a].add(pais_b)
                     paises[pais_b].add(pais_a)

        print ("paises: ", paises)
        
        dijkstra(graph, 1, 2)

        for _ in xrange(k):
            # dijkstra
            # se agencia no mesmo pais entao gasto eh 0
            u, v = map(int, raw_input().split())
            
