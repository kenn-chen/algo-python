def change(coins, n):
	m = len(coins)
	dp = [[0]*(n+1) for _ in range(m)]
	for i in range(m): dp[i][0] = 1

	for i in range(m):
		for j in range(1, n+1):
			dp1 = dp[i-1][j] if i >= 1 else 0
			dp2 = dp[i][j-coins[i]] if j >= coins[i] else 0
			dp[i][j] = dp1 + dp2
	return dp[-1][-1]