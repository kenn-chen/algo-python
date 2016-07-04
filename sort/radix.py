def sort(nums):
	base, exp = 10, 1
	max_num = max(nums)
	while max_num//exp > 0:
		_counting_sort(nums, exp, base)
		exp *= base
		
def _counting_sort(nums, exp, base):
	output = [0] * len(nums)
	count = [0] * base
	index = lambda i: (i//exp)%base

	for i in nums:
		count[index(i)] += 1
	for i in range(1, len(count)):
		count[i] += count[i-1]
	for i in range(len(nums)-1, -1, -1):
		num = nums[i]
		pos = count[index(num)] - 1
		output[pos] = num
		count[index(num)] -= 1
	nums[:] = output