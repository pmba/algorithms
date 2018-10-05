def knapsack(i, rc, memo, c, n, prices, weight):
    if memo[i][rc] != -1:
        return memo[i][rc]
    if i == n:
        memo[i][rc] = 0
    elif rc == 0:
        memo[i][rc] = 0
    elif weight[i] > rc:
        memo[i][rc] = knapsack(i+1, rc, memo, c, n, prices, weight)
    else:
        memo[i][rc] = max(prices[i] + knapsack(i+1, rc-weight[i], memo, c, n, prices, weight), knapsack(i+1, rc, memo, c, n, prices, weight))
    return memo[i][rc]

cases = int(input())

for _ in range(cases):
    products = int(input())
    prices = []
    weight = []
    for _ in range(products):
        p, w = map(int, input().split())
        prices.append(p)
        weight.append(w)
    
    person = int(input())
    max_value = 0
    for _ in range(person):
        capacity = int(input())
        memo = [[-1 for i in range(capacity+1)] for j in range(products+1)]
        max_value += knapsack(0, capacity, memo, capacity, products, prices, weight)
    print(max_value)

