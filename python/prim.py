import heapq

DEBUG = 1

graph =[
    [[2,1],[3,2]],
    [[2,0],[5,2],[5,3]],
    [[5,1],[7,3],[4,4],[3,0]],
    [[5,1],[7,2],[4,4]],
    [[4,2],[4,3]]
]

def print_graph(graph):
    for v in graph:
        print(v)

def add_vertex(graph, v1, v2, cost):
    graph[v1].append([cost, v2])
    graph[v2].append([cost, v1])

def mst(graph, start):
    size = len(graph)
    visited = [0 for x in range(size)]
    heap = []
    new_graph = [[] for x in range(size)]
    total_cost = 0

    visited[start] = 1
    heapq.heappush(heap, [0, (0, 0)])
    
    while heap:
        info = heapq.heappop(heap)
        cur_cost = info[0]
        origin = info[1][0]
        destination = info[1][1]
        visited[destination] = 1        

        if not origin == destination:
            total_cost += cur_cost
            if DEBUG: print(origin, destination)
            add_vertex(new_graph, origin, destination, cur_cost)
        
        if sum(visited) == size:
            print('MST Cost:', total_cost)
            return new_graph

        for vertex in range(len(graph[destination])):
            edge_cost = graph[destination][vertex][0]
            edge_to = graph[destination][vertex][1]

            if not visited[edge_to]:
                heapq.heappush(heap, [edge_cost, (destination, edge_to)])


new_graph = mst(graph, 0)
print_graph(new_graph)