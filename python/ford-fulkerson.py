class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for row in range(vertices)]
    
    def add_vertex(self, u, v, c):
        self.graph[u][v] = c

    def print_graph(self):
        for row in self.graph:
            print(row)

    def bfs(self, s, t, parent):
        visited = [0]*self.V
        queue = []
        queue.append(s)
        visited[s] = 1

        while queue:
            u = queue.pop()
            for i, v in enumerate(self.graph[u]):
                if not visited[i] and v > 0:
                    queue.append(i)
                    visited[i] = 1
                    parent[i] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1]*self.V
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


g = Graph(4)
g.add_vertex(0, 1, 3)
g.add_vertex(0, 2, 2)
g.add_vertex(1, 2, 5)
g.add_vertex(1, 3, 2)
g.add_vertex(2, 3, 3)

g.print_graph()
print(g.ford_fulkerson(0, 3))
g.print_graph()