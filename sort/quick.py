def sort(nums):
	_sort(nums, 0, len(nums)-1)

def _sort(nums, low, high):
	if low < high:
		p = _partition(nums, low, high)
		_sort(nums, low, p-1)
		_sort(nums, p+1, high)

def _partition(nums, low, high):
	pivot = nums[low]
	l, r  = low + 1, high

	while l <= r:
		while l<=r and nums[l]<=pivot: l += 1
		while l<=r and nums[r]>=pivot: r -= 1
		if l < r:
			nums[l], nums[r] = nums[r], nums[l]
			
	nums[low], nums[r] = nums[r], nums[low]
	return r