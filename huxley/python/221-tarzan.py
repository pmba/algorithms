import math
DEBUG = 0

class UnionFind:
    def __init__(self):
        self.parent = {}

    def insert(self, u):
        self.parent[u] = -1
    
    def root(self, u):
        if isinstance(self.parent[u], int):
            return u
        else:
            self.parent[u] = self.root(self.parent[u])
            return self.parent[u]

    def same_set(self, u, v):
        return self.root(u) == self.root(v)

    def merge(self, u, v):
        ur = self.root(u)
        vr = self.root(v)

        if ur == vr:
            return

        if DEBUG: print(u, v)

        if isinstance(self.parent[ur], int) and isinstance(self.parent[vr], int):
            if self.parent[ur] < self.parent[vr]:
                aux = self.parent[ur]
                self.parent[ur] = self.parent[vr]
                self.parent[vr] = aux

            self.parent[vr] += self.parent[ur]
            self.parent[ur] = vr


def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

UF = UnionFind()
trees, max_distance = map(int, input().split())
coordinate = []

for _ in range(trees):
    xcord, ycord = map(int, input().split())
    UF.insert((xcord, ycord))
    coordinate.append((xcord, ycord))

for i in range(trees):
    for j in range(trees):
        if not i == j:
            if distance(coordinate[i], coordinate[j]) <= max_distance:
                UF.merge(coordinate[i], coordinate[j])

same_set = 1
first_c = coordinate[0]
for c in coordinate:
    if not UF.same_set(first_c, c):
        same_set = 0
        print('N')
        break

if same_set:
    print('S')

    