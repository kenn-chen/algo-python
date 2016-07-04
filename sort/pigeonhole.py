def sort(nums):
	max_num, min_num = max(nums), min(nums)
	interval = max_num - min_num + 1
	holes = [[] for _ in range(interval)]
	for num in nums:
		holes[num-min_num].append(num)
	i = 0
	for hole in holes:
		nums[i:i+len(hole)] = hole
		i += len(hole)
