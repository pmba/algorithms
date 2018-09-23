nel = 3
cap = 26

memo = [[-1 for x in range(nel+1)] for y in range(cap+1)]

price = [72, 44, 31]
weight = [17, 23, 24]

def dp(i, rc):
    if not memo[i][rc] == -1: return memo[i][rc]
    if i == nel: memo[i][rc] = 0
    elif rc == 0: memo[i][rc] = 0
    elif weight[i] > rc: memo[i][rc] = dp(i+1, rc)
    else: memo[i][rc] = max(price[i] + dp(i+1, rc - weight[i]), dp(i+1, rc))
    return memo[i][rc]

print(dp(0, cap-1))