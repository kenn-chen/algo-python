def sort(nums):
	_sort(nums, 0, len(nums)-1)

def _sort(nums, l, r):
	if l < r:
		m = (l + r) // 2
		_sort(nums, l, m)
		_sort(nums, m+1, r)
		_merge(nums, l, m, r)

def _merge(nums, l, m, r):
	n1, n2 = m-l+1, r-m
	L, R   = [0]*n1, [0]*n2
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
	while i < n1: nums[l+i+j] = L[i]; i+= 1
	while j < n2: nums[l+i+j] = R[j]; j+= 1