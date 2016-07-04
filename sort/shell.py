def sort(nums):
	gaps = []
	k = 1
	while (3**k-1)//2 < len(nums):
		gaps.append((3**k-1)//2)
		k += 1
		
	k = len(gaps) - 1
	while k >= 0:
		gap = gaps[k]
		for i in range(gap, len(nums)):
			j = i
			while j>=gap and nums[j]<nums[j-gap]:
				nums[j], nums[j-gap] = nums[j-gap], nums[j]
				j -= gap
		k -= 1