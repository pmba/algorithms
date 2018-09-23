import heapq

def dijkstra(ini, end):
    visited = [0 for x in range(cities_quant * 2)]
    toll = [float('inf') for x in range(cities_quant * 2)]
    heap = []

    toll[ini] = 0
    heapq.heappush(heap, [0, 0])

    while heap:
        current_city = heapq.heappop(heap)[1]

        if not visited[current_city]:
            visited[current_city] = 1

            for v in range(len(roads[current_city])):
                next_city = roads[current_city][v][1]
                city_toll = roads[current_city][v][0]

                if toll[current_city] + city_toll < toll[next_city]:
                    toll[next_city] = toll[current_city] + city_toll
                    heapq.heappush(heap, [toll[next_city], next_city])

    return toll
    

DEBUG = 1

cities_quant, roads_quant = [int(x) for x in input().split()]
roads = [[] for x in range(cities_quant * 2)]

for i in range(roads_quant):
    origin, destination, cost = [int(x) for x in input().split()]
    
    o1 = 2 * origin - 1
    d1 = 2 * destination - 1

    o2 = o1 + 1
    d2 = d1 + 1

    roads[o1 - 1].append([cost, d2 - 1])
    roads[d2 - 1].append([cost, o1 - 1])
    roads[o2 - 1].append([cost, d1 - 1])
    roads[d1 - 1].append([cost, o2 - 1])

toll_res = dijkstra(0, cities_quant * 2 - 1)

if (toll_res[-2] == float('inf')):
    print(-1)
else:
    print(toll_res[-2])
