def count(nums):
	return merge(nums, 0, len(nums)-1)

def merge(nums, l, r):
	if l == r: return 0

	mid = (l + r) // 2
	inv_count = 0

	inv_count += merge(nums, l, mid)
	inv_count += merge(nums, mid+1, r)
	inv_count += __merge(nums, l, mid, r)
	return inv_count

def __merge(nums, l, m, r):
	inv_count = 0
	n1, n2 = m-l+1, r-m
	L, R = [0]*n1, [0]*n2
	for i in range(n1): L[i] = nums[l+i]
	for i in range(n2): R[i] = nums[m+1+i]

	i = j = 0
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			nums[l+i+j] = L[i]
			i += 1
		else:
			nums[l+i+j] = R[j]
			j += 1
			inv_count += m-(l+i)+1
	while i < n1:
		nums[l+i+j] = L[i]
		i += 1
	while j < n2:
		nums[l+i+j] = R[j]
		j += 1

	return inv_count