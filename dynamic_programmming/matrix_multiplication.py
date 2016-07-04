def mp(p):
	MAX = 0x7FFFFFFF
	n = len(p)-1
	dp = [[0]*n for _ in range(n)]

	for l in range(2, n+1):
		for i in range(0, n-l+1): #n-1-x+1 = l ==> x=n-l
			j = i + l - 1
			dp[i][j] = MAX
			for k in range(i, j):
				_dp = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
				dp[i][j] = min(dp[i][j], _dp)
	return dp[0][-1]
