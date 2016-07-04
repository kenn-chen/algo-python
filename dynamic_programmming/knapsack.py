def knapsack(W, wts, vals):
	N = len(vals)
	dp = [[0] * (W+1) for i in range(N+1)]
	for n in range(1, N+1):
		for w in range(1, W+1):
			if wts[n-1] > W:
				dp[n][w] = dp[n-1][w]
			else:
				dp[n][w] = max(dp[n-1][w-wts[n-1]]+vals[n-1], dp[n-1][w])
	return dp[N][W]

if __name__ == "__main__":
	W = 20
	wts  = [1, 3, 5, 4, 7, 5, 8, 3, 9, 3]
	vals = [2, 5, 4, 7, 8, 1, 4, 3, 7, 5]
	print(knapsack(W, wts, vals))
