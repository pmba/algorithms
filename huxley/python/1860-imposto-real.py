from queue import Queue
DEBUG = 1

cities, capacity = [int(x) for x in input().split()]
graph = [[] for x in range(cities)]

tax = [int(x) for x in input().split()]

for i in range(cities-1):
    a, b, c = [int(x) for x in input().split()]
    graph[a-1].append([b-1, c])
    graph[b-1].append([a-1, c])

def dfs(n, p):
    total_kilometers = 0
    total_money = tax[n]

    for v in range(len(graph[n])):
        next_city = graph[n][v][0]
        if next_city == p: continue
        next_city_info = dfs(next_city, n)
        next_city_money = next_city_info[1]
        next_city_kilometers = next_city_info[0]
        how_many_trips = (next_city_money + capacity - 1)//capacity
        total_kilometers += next_city_kilometers
        total_kilometers += graph[n][v][1] * how_many_trips
        total_money += next_city_money
    
    return [total_kilometers, total_money]

print(dfs(0, 0)[0] << 1)

