import heapq

class UnionFind:
    def __init__(self, size):
        self.parent = [-1 for x in range(size)]

    def root(self, v):
        if self.parent[v] < 0:
            return v
        else:
            self.parent[v] = self.root(self.parent[v])
            return self.parent[v]

    def sameSet(self, v, u):
        return self.root(v) == self.root(u)

    def merge(self, v, u):
        v = self.root(v)
        u = self.root(u)

        if v == u: 
            return

        if self.parent[u] < self.parent[v]:
            aux = self.parent[u]
            self.parent[u] = self.parent[v]
            self.parent[v] = aux

        self.parent[v] += self.parent[u]
        self.parent[u] = v

class Graph:
    def __init__(self, vertices):
        self.cost = 0
        self.V = vertices
        self.graph = [[] for i in range(vertices)]
    
    def addEdge(self, u, v, w):
        self.cost += w
        self.graph[u].append([v, w])
        self.graph[v].append([u, w])

    def printGraph(self):
        for i in range(len(self.graph)):
            print(i, '-', self.graph[i])

G = Graph(4)
UF = UnionFind(4)
Q = []

G.addEdge(0, 1, 2)
heapq.heappush(Q, [2, 0, 1])
G.addEdge(0, 3, 5)
heapq.heappush(Q, [5, 0, 3])
G.addEdge(1, 2, 1)
heapq.heappush(Q, [1, 1, 2])
G.addEdge(1, 3, 4)
heapq.heappush(Q, [4, 1, 3])
G.addEdge(2, 3, 3)
heapq.heappush(Q, [3, 2, 3])

print('\nGraph Cost:', G.cost)
G.printGraph()

mst_cost = 0
MST = Graph(4)

while Q:
    cost, origin, destination = heapq.heappop(Q)
    if not UF.sameSet(origin, destination):
        MST.addEdge(origin, destination, cost)
        UF.merge(origin, destination)

print('\nMST Cost:', MST.cost)
MST.printGraph()
