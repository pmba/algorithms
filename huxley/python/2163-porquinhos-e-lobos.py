class Animal:
    def __init__(self):
        self.Q = 0
        self.A = {}

    def put(self, cord, index):
        self.A[cord] = index
        self.Q += 1

row, col = map(int, input().split())

pigs = Animal()
wolfs = Animal()
field = []

def find_pig_to_eat(field, i, j):
    res = []

    if i > 0 and field[i-1][j] == 'P':
        res.append((i-1, j))
    if i < row-1 and field[i+1][j] == 'P':
        res.append((i+1, j))
    if j > 0 and field[i][j-1] == 'P':
        res.append((i, j-1))
    if j < col-1 and field[i][j+1] == 'P':
        res.append((i, j+1))

    return res

index = 0

for i in range(row):
    field.append(list(input()))
    for j in range(len(field[i])):
        if field[i][j] == 'P':
            pigs.put((i, j), index)
            index += 1
        elif field[i][j] == 'W':
            wolfs.put((i, j), index)
            index += 1

graph = [[0 for j in range(pigs.Q+wolfs.Q)] for i in range(pigs.Q+wolfs.Q)]

for key, wolf_index in wolfs.A.items():
    food = find_pig_to_eat(field, key[0], key[1])
    for pig in food:
        pig_index = pigs.A[pig]
        graph[wolf_index][pig_index] = 1

def bfs(s, t, parent):
    visited = [False]*len(graph)
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for index, val in enumerate(graph[u]):
            if not visited[index] and val > 0:
                queue.append(index)
                visited[index] = True
                parent[index] = u
    
    return True if visited[t] else False


def ford_fulkerson(source, sink):
    parent = [-1]*len(graph)
    max_flow = 0

    while bfs(source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    print(parent)
    return max_flow

for x in graph:
    print(x)

first_wolf = list(wolfs.A.values())[0]
print(ford_fulkerson(first_wolf, len(graph)-1))




        



