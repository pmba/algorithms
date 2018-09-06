import heapq

def add_vertex(origin, destin):
	bridges[origin-1].append(destin-1)
	bridges[destin-1].append(origin-1)

def dijkstra(ini, end):
	distance = [float('inf') for x in bridges]
	visited = [0 for x in bridges]
	heap = []

	distance[ini] = 0
	visited[ini] = 1
	heapq.heappush(heap, (distance[ini], ini))

	while heap:
		island_distance, island = heapq.heappop(heap)
		visited[island] = 1

		if island == end:
			return island_distance

		for vertex in bridges[island]:
			if not visited[vertex]:
				if island_distance+1 < distance[vertex]:
					distance[vertex] = island_distance+1
					heapq.heappush(heap, (distance[vertex], vertex))

	return -1

cases = int(input())

for i in range(cases):
	island_quant, bridge_quant = [int(x) for x in input().split()]
	bridges = [[] for x in range(island_quant)]
	
	for j in range(bridge_quant):
		origin_island, destin_island = [int(x) for x in input().split()]
		add_vertex(origin_island, destin_island)
	print(dijkstra(0, island_quant-1))
