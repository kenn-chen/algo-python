def LIS(nums):
	return __LIS1(nums)

def __LIS1(nums):
	n = len(nums)
	dp = [1] * n
	for i in range(1, n):
		for j in range(0, i):
			if nums[i] > nums[j] and dp[i] < dp[j]+1:
				dp[i] = dp[j] + 1
	return max(dp)


def __LIS2(nums):
	if not nums: return []

	seq = [nums[0]]
	for num in nums[1:]:
		if num > seq[-1]:
			seq.append(num)
		elif num < seq[-1]:
			index = search(seq, num)
			seq[index] = num
	return len(seq)



def __search(seq, k):
	l, r = 0, len(seq)-1
	while l < r:
		m = (l + r) // 2

		if seq[m] == k:
			return m
		elif seq[m] < k:
			l = m + 1
		else:
			r = m
	return l