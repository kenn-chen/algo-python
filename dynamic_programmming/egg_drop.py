def drop(f, e):
	MAX = 0x7FFFFFFF
	dp = [[0]*(f+1) for _ in range(e+1)]
	for i in range(1, f+1): dp[1][i] = i
	for i in range(1, e+1): dp[i][1] = 1

	for i in range(2, e+1):
		for j in range(2, f+1):
			dp[i][j] = MAX
			for x in range(1, j+1):
				_dp = 1 + max(dp[i-1][x-1], dp[i][j-x])
				dp[i][j] = min(dp[i][j], _dp)
	return dp[-1][-1]
		