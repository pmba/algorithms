import heapq

DEBUG = 0


def print_graph(graph):
    for i in range(len(graph)):
        print(i, '-', graph[i])


def init_graph():
    graph = [[], [], [], [], [], []]

    graph[0].append(1)
    graph[0].append(2)
    graph[0].append(3)
    graph[1].append(0)
    graph[1].append(2)
    graph[2].append(0)
    graph[2].append(1)
    graph[2].append(5)
    graph[3].append(0)
    graph[3].append(4)
    graph[4].append(3)
    graph[4].append(5)
    graph[5].append(2)
    graph[5].append(4)

    return graph


def dijkstra(graph, orig, dest):
    distance = [float('inf') for x in graph]
    visited = [0 for x in graph]
    heap = []
    distance[orig] = 0
    visited[orig] = 1
    heapq.heappush(heap, (distance[orig], orig))

    while heap:
        current_distance, current = heapq.heappop(heap)

        if DEBUG:
            print('Current', current)

        visited[current] = 1
        if current == dest:
            print('From', orig, 'to', dest, 'with distance', current_distance)
            return current_distance

        for v in graph[current]:
            if not visited[v]:
                if current_distance+1 < distance[v]:
                    distance[v] = current_distance+1
                    heapq.heappush(heap, (distance[v], v))


gr = init_graph()

print_graph(gr)

print()
start = int(input('Origin: '))
end = int(input('Destination: '))

print()
dijkstra(gr, start, end)
