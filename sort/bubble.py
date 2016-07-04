def sort(nums):
	size = len(nums)
	for i in range(size-1):
		for j in range(size-1-i):
			if nums[j+1] < nums[j]:
				nums[j], nums[j+1] = nums[j+1], nums[j]