D, P, R, B = map(int, input().split())
prices = []
pd = [int(x) for x in input().split()]

for p in pd:
    prices.append(p)

prism = [int(x) for x in input().split()]

for p in prism:
    prices.append(p)

riv = [[0 for x in range(P+D)] for x in range(P+D)]

for i in range(R):
    X, Y = map(int, input().split())
    riv[X-1][(Y+D)-1] = 1
    riv[(Y+D)-1][X-1] = 1

groups = []
visited = [0]*(D+P)

def update_group(group, u):
    if u < D:
        group[0] += 1
    else:
        group[1] += 1
    group[2] += prices[u]

    return group

def dfs(u, group):
    visited[u] = 1

    for i, w in enumerate(riv[u]):
        if not visited[i] and w == 1:
            group = update_group(group, i)
            
            return dfs(i, group)

    return group


for i in range(len(riv)):
    if not visited[i]:
        group = [0,0,0]
        group = update_group(group, i)
        groups.append(dfs(i, group))

print(groups)

memo = [[[-1,-1] for j in range(B+1)] for i in range(len(groups) + 1)]

def knapsack(i, w):
    if memo[i][w] == [-1,-1]:
        if i == len(groups) or w == 0:
            memo[i][w] = [0,0]
        elif prices[i] > B:
            memo[i][w] = knapsack(i+1, w)
        else:
            memo[i][w] = max(prices[i] + knapsack(i+1, w-prices[i])[2], knapsack(i+1, w)[2])
    return memo[i][w]

print(knapsack(0, B))

    

