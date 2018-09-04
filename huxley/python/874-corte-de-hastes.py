# def find_max_value(bar):
# 	memo = [0 for i in range(bar+1)]

# 	for i in range(1, bar+1):
# 		best_case = 0
# 		for j in range(i):
# 			best_case = max(best_case, prices[j]+memo[i-j-1])
# 		memo[i] = best_case
# 	return memo[bar]

def find_max_rec_value(bar):
	if bar == 0:
		return 0
	if not memo[bar] == -1:
		return memo[bar]

	max_val = -1
	for i in range(1, bar+1):
		max_val = max(max_val, prices[i]+find_max_rec_value(bar-i))
	memo[bar] = max_val
	return max_val

while True:
	bar_len = int(input())
	
	if bar_len == 0:
		break
		
	prices = [0]
	prices += [int(input()) for i in range(bar_len)]
	memo = [-1 for i in range(bar_len+1)]

	print(find_max_rec_value(bar_len))