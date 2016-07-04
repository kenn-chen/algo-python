def partition(s):
	MAX = 0x7FFFFFFF
	n = len(s)
	dp = [[0]*n for _ in range(n)]

	for l in range(2, n+1):
		for i in range(0, n-l+1):
			j = i + l - 1

			if s[i] == s[j] and dp[i+1][j-1] == 0:
				dp[i][j] = 0
			else:
				dp[i][j] = MAX
				for k in range(i, j):
					dp[i][j] = min(dp[i][j], 1+dp[i][k]+dp[k+1][j]) 
	return dp[0][-1]