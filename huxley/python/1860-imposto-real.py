from queue import *

DEBUG = 1

def bfs(u):
    global graph


cidades, capacidade = [int(x) for x in input().split()]
graph = [[] for x in range(cidades)]

imposto = [int(x) for x in input().split()]

for i in range(cidades-1):
    a, b, c = [int(x) for x in input().split()]
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

if DEBUG:
    print(graph)
