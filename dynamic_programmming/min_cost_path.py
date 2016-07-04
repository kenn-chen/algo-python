def path(cost):
	m, n = len(cost), len(cost[0])
	dp = [[0]*n for _ in range(m)]

	dp[0][0] = cost[0][0]
	for i in range(1, m): dp[i][0] = dp[i-1][0] + cost[i][0]
	for i in range(1, n): dp[0][i] = dp[0][i-1] + cost[0][i]

	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + cost[i][j]
	return dp[-1][-1]