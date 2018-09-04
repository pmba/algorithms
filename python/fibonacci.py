#bottom_up

def fib_bu(n):
	if n <= 2:
		return n

	memo = [0 for i in range(n+1)]
	memo[0] = 0
	memo[1] = 1
	memo[2] = 1

	for i in range(2, n+1):
		memo[i] = memo[i-1]+memo[i-2]
	return memo[n]

print('Fibonnacci =',fib(int(input())))

