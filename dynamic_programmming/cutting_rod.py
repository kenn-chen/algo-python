def cut(size, prices):
	n = len(prices)
	dp = [0] * (n + 1)

	for i in range(1, n+1):
		dp[i] = prices[i-1]
		for j in range(1, i//2+1):
			dp[i] = max(dp[i], dp[j]+dp[i-j])

	return dp[n]