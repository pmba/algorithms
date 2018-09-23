import heapq

DEBUG = 0

def dijkstra(ini):
    visited = [0 for x in range(houses)]
    distance = [float('inf') for x in range(houses)]

    distance[ini] = 0

    heap = []
    heapq.heappush(heap, [0, 0])

    while heap:
        time_from_ini, current_house = heapq.heappop(heap)

        if visited[current_house]:
            continue

        visited[current_house] = 1

        for v in range(len(roads[current_house])):
    
            next_house = roads[current_house][v][1]
            time_to_next_house = roads[current_house][v][0]

            if distance[current_house] + time_to_next_house < distance[next_house]:
                distance[next_house] = distance[current_house] + time_to_next_house
                heapq.heappush(heap, [distance[next_house], next_house])
    
    return distance




cases = int(input())
index = 1

while cases:
    houses, road_quant = [int(x) for x in input().split()]
    roads = [[] for x in range(houses)]
    
    while road_quant:
        origin, destination, time = [int(x) for x in input().split()]
        roads[origin-1].append([time, destination-1])
        roads[destination-1].append([time, origin-1])
        road_quant -= 1
    
    orders_quant = int(input())
    orders_adresses = [int(x) for x in input().split()]

    if DEBUG: print(roads)

    order_time = dijkstra(0)

    if DEBUG: print(order_time)

    total_time = 0
    for k in range(orders_quant):
        total_time += order_time[orders_adresses[k]-1]

    print('case %d: %d' % (index, total_time*2))

    index += 1
    cases -= 1

