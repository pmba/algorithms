import heapq
DEBUG = 0

def prim(graph, ini):
    visited = [0 for i in range(len(graph))]
    queue = []
    mst = [[] for i in range(len(graph))]

    visited[ini] = 1
    heapq.heappush(queue, [0, ini, 0])

    mst_cost = 0

    while queue:
        cur_weight, cur_vertex, cur_previous = heapq.heappop(queue)
        
        if not visited[cur_vertex]:
            visited[cur_vertex] = 1
            mst_cost += cur_weight
            mst[cur_vertex].append([cur_weight, cur_previous])
            mst[cur_previous].append([cur_weight, cur_vertex])
            if DEBUG: print(cur_vertex, cur_weight, cur_previous)
            


        for v in range(len(graph[cur_vertex])):
            edge_to = graph[cur_vertex][v]
            if not visited[edge_to[1]]:
                heapq.heappush(queue, [edge_to[0], edge_to[1], cur_vertex])

    return mst, mst_cost
    

vertices, edges = map(int, input().split())
graph = [[] for i in range(vertices)]

while edges:
    origin, destination, weight = map(int, input().split())
    graph[origin].append([weight, destination])
    graph[destination].append([weight, origin])
    edges -= 1

if DEBUG:
    for x in graph: print(x)

mst, mst_cost = prim(graph, 4)
for x in mst:
    print(x)

print('MST Cost:', mst_cost)