import heapq
DEBUG = 0

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

vertices, edges = map(int, input().split())
graph = [[] for x in range(vertices)]
queue = []
uf = UnionFind(vertices)
total_cost = 0

while edges:
    origin, destination, cost = map(int, input().split())
    graph[origin-1].append([cost, destination-1])
    graph[destination-1].append([cost, origin-1])
    heapq.heappush(queue, [cost, origin-1, destination-1])
    edges -= 1

while queue:
    info = heapq.heappop(queue)
    if not uf.sameSet(info[1], info[2]):
        total_cost += info[0]
        uf.merge(info[1], info[2])

print(total_cost)
    
