from queue import Queue

graph = [
    [1, 4],
    [2, 4],
    [3],
    [],
    [],
    [4],
    [2, 7],
    [3],
    []
]

def indegree(graph):
    ind = [0 for x in range(len(graph))]

    for v in graph:
        for adj in range(len(v)):
            ind[v[adj]] += 1

    return ind

def recalc_indegree(u, indegree):
    for v in u:
        if indegree[v] > 0:
            indegree[v] -= 1
    return indegree


def kahn(graph, indegree):
    queue = Queue()
    awnser = []

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.put(i)

    while not queue.empty():
        u = queue.get()
        awnser.append(u)
        indegree = recalc_indegree(graph[u], indegree)
        
        for v in graph[u]:
            if indegree[v] == 0:
                queue.put(v)
        
        graph[u] = []

    print(awnser)

vertex_indegree = indegree(graph)
kahn(graph, vertex_indegree)

