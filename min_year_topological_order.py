from collections import defaultdict

def topological_order(graph):
    count = defaultdict(int)
    zero_in = []
    top_sort = []

    for node, adjacents in graph.items():
        for adj in adjacents:
            count[adj] += 1

    for node in graph.keys():
        if count[node] == 0:
            zero_in.append(node)

    if len(zero_in) == 0:
        raise Exception("There is no node with zero in-degree")

    while len(zero_in):
        removed_node = zero_in.pop()
        top_sort.append(removed_node)
        del count[removed_node]
    
        for node in graph[removed_node]:
            count[node] -= 1

            if count[node] == 0:
                zero_in.append(node)

    if len(count):
        raise Exception("This graph does not have a topological order")

    return top_sort
    
def reverse_graph(graph):
    rev = dict()
    for node, adjacents in graph.items():
        for adj in adjacents:
            try:
                rev[adj].add(node)
            except KeyError:
                rev[adj] = set()
            rev[adj].add(node)
    return rev

def find_min_years(top_order, graph):
    reverse = reverse_graph(graph) 
    distances = {x: 0 for x in graph.keys()}
    year = 0

    for num in top_order:
        maximum_time = 1
        try:
            for adj in reverse[num]:
                maximum_time = max(maximum_time, distances[adj] + 1)
        except KeyError:
            pass
        distances[num] = maximum_time

    return distances[top_order[-1]]



if __name__ == '__main__':
    graph = {
        3: {2,4},
        2: {4},
        1: {4},
        4: {}
    }
    
    graph2 = {
        3: {2,4},
        2: {1,4},
        1: {4},
        4: {}
    }

    graph3 = {
        3: {2,4},
        2: {1,4},
        1: {4},
        4: {},
        5: {2},
        6: {5}
    }

    top_order = topological_order(graph)
    top_order2 = topological_order(graph2)
    top_order3 = topological_order(graph3)

    try:
        assert find_min_years(top_order, graph) ==  3
        assert find_min_years(top_order2, graph2) ==  4
        assert find_min_years(top_order3, graph3) ==  5
        print "Tests passed"
    except AssertionError:
        print "Tests failed"
        
