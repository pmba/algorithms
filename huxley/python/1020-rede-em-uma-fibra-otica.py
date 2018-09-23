import heapq
DEBUG = 0

def add_edge(graph, ori, end, cost):
    graph[ori].append([cost, end])
    graph[end].append([cost, ori])

vertex, edges, velocity = map(int, input().split())
graph = [[] for x in range(vertex)]

while edges:
    origin, destination, distance = map(int, input().split())
    add_edge(graph, origin, destination, distance)
    edges -= 1

if DEBUG: 
    for v in graph: print(v)

def dijkstra(graph, ini, end):
    size = len(graph)
    distance = [float('inf') for x in range(size)]
    visited = [0 for x in range(size)]
    heap = []

    distance[ini] = 0
    heapq.heappush(heap, [distance[ini], ini])

    while heap:
        cur_distance, cur_vertex = heapq.heappop(heap)
        visited[cur_vertex] = 1

        if (cur_vertex == end):
            return distance[cur_vertex]

        for v in range(len(graph[cur_vertex])):
            vertex_cost, vertex_to = graph[cur_vertex][v]

            if not visited[vertex_to]:
                if distance[cur_vertex] + vertex_cost < distance[vertex_to]:
                    distance[vertex_to] = distance[cur_vertex] + vertex_cost
                    heapq.heappush(heap, [distance[vertex_to], vertex_to])

def mst(graph, start):
    size = len(graph)
    visited = [0 for x in range(size)]
    distance = [float('inf') for x in range(size)]
    heap = []
    new_graph = [[] for x in range(size)]
    ping_con = []
    total_cost = 0

    visited[start] = 1
    distance[start] = 0
    heapq.heappush(heap, [0, (0, 0)])
    
    while heap:
        info = heapq.heappop(heap)
        cur_cost = info[0]
        origin = info[1][0]
        destination = info[1][1]
        visited[destination] = 1        

        if not origin == destination:
            total_cost += cur_cost

            if DEBUG: 
                print(distance)
                print(origin, destination)

            ping_con.append([origin, destination])
            add_edge(new_graph, origin, destination, cur_cost)
        
        if sum(visited) == size:
            if DEBUG: print('MST Cost:', total_cost)
            return total_cost, ping_con, new_graph

        for vertex in range(len(graph[destination])):
            edge_cost = graph[destination][vertex][0]
            edge_to = graph[destination][vertex][1]

            if not visited[edge_to]:
                if distance[destination] + edge_cost < distance[edge_to]:
                    distance[edge_to] = distance[destination] + edge_cost
                heapq.heappush(heap, [edge_cost, (destination, edge_to)])

mst_cost, info, new_graph = mst(graph, 0)

for x in info:
    if x[0] > x[1]:
        aux = x[0]
        x[0] = x[1]
        x[1] = aux
        
info.sort(key=lambda x: (x[0], x[1]))
for x in info:
    print(x)

if DEBUG: print(mst_cost)
if DEBUG: print(info)

print('########################')
print('Minimum Cost:')
print(mst_cost)
print('########################')
print('Connections:')

for x in range(len(info)):
    print(info[x][0], info[x][1])

print('########################')
print('Pings:')

for x in range(1, vertex):
    print('%d: %.3f' % (x, (dijkstra(new_graph, 0, x) * 2)/velocity))

print('########################') 

