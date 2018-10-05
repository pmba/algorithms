import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[[0,-1] for col in range(vertices)] for row in range(vertices)]
    
    def add_vertex(self, u, v, c, d):
        self.graph[u][v] = [c,d]

    def print_graph(self):
        for row in self.graph:
            print(row)

    def bfs(self, s, t, parent, path):
        visited = [1]*self.V
        queue = []
        queue.append(s)

        for i in path:
            visited[i] = 0

        visited[s] = 1

        while queue:
            u = queue.pop()
            for i, v in enumerate(self.graph[u]):
                if not visited[i] and v[0] > 0:
                    queue.append(i)
                    visited[i] = 1
                    parent[i] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink, path):
        parent = [-1]*self.V
        max_flow = 0

        while self.bfs(source, sink, parent, path):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s][0])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v][0] -= path_flow
                self.graph[v][u][0] += path_flow
                v = parent[v]

        return max_flow

    def dijkstra(self, u, v):
        distance = [float('inf')]*self.V
        visited = [0]*self.V
        heap = []
        distance[u] = 0
        visited[u] = 1
        heapq.heappush(heap, (distance[u], u))
        path = []
        
        while heap:
            cd, c = heapq.heappop(heap)
            path.append(c)
            if c == v:
                return distance[c], path
            
            for w, d in enumerate(self.graph[c]):
                if d[1] != -1:
                    if not visited[w]:
                        if cd+d[1] < distance[w]:
                            distance[w] = cd+d[1]
                            visited[w] = 1
                            heapq.heappush(heap, (distance[w], w))


vertices = int(input())
cities = int(input())
locates = []

for i in range(cities):
    locates.append([int(x) for x in input().split()])

g = Graph(vertices)
edges = int(input())

for i in range(edges):
    u, v, c, d = map(int, input().split())
    g.add_vertex(u,v,c,d)


origin, destination = map(int, input().split())
distance, path = g.dijkstra(origin, destination)
max_flow = g.ford_fulkerson(origin, destination, path)

print(path)
print(distance)
print(max_flow)