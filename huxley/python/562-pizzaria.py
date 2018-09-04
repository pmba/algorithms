import heapq


def add_egde(v1, v2, length, graph):
    graph[v1].append([length, v2])
    graph[v2].append([length, v1])


def print_graph(graph):
    for i in range(len(graph)):
        print(i, '-', graph[i])


def dijkstra(graph, orig, dest):
    visited = [0 for x in graph]
    pq = []
    visited[orig] = 1
    heapq.heappush(pq, [0, orig])

    while pq:
        current_distance, current = heapq.heappop(pq)

        visited[current] = 1

        if current == dest:
            return current_distance

        for v in graph[current]:
            if not visited[v[1]]:
                v[0] += current_distance
                heapq.heappush(pq, v)


cases = int(input())

for i in range(cases):
    vertex, edges = [int(x) for x in input().split()]
    graph = [[] for x in range(vertex+1)]

    for j in range(edges):
        v1, v2, length = [int(x) for x in input().split()]
        add_egde(v1, v2, length, graph)

    input()
    order = [int(x) for x in input().split()]
    total_time = 0

    for j in range(len(order)):
        total_time += dijkstra(graph, 1, order[j]) * 2

    print('caso %d: %d' % (i+1, total_time))

