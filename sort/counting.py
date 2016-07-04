def sort(nums):
	output = [0] * len(nums)
	min_num, max_num = min(nums), max(nums)
	if (max_num - min_num) / len(nums) > 100: 
		return print("Not suitable for counting sort")

	index = lambda i: i -min_num
	count = [0] * (max_num-min_num+1)
	
	for i in nums:
		count[index(i)] += 1
	for i in range(1, len(count)):
		count[i] += count[i-1]
	for i in nums:
		pos = count[index(i)] - 1
		output[pos] = i
		count[index(i)] -= 1
	nums[:] = output