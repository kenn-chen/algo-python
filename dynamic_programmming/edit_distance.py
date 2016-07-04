# insertion cost: 		1
# deletion cost:		1
# substitution cost: 	2

def distance(s1, s2):
	m, n = len(s1), len(s2)
	dp = [[0]*(n+1) for _ in range(m+1)]
	for i in range(m): dp[i][0] = i
	for i in range(n): dp[0][i] = i

	for i in range(1, m+1):
		for j in range(1, n+1):
			if s1[i-1] == s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
	return dp[m][n]
