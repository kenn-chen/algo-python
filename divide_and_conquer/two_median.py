def __median(nums):
	n = len(nums)
	if n % 2 == 0:
		return (nums[n//2-1] + nums[n//2]) / 2
	else:
		return nums[n//2]

def median(nums1, nums2):
	n = len(nums1)
	if n == 1: return (nums1[0] + nums2[0]) / 2
	if n == 2: return (max(nums1[0], nums2[0]) + min(nums1[1], nums2[1])) / 2

	m1, m2 = __median(nums1), __median(nums2)
	if m1 == m2: return m1

	if m1 < m2: 
		smaller = nums1
		larger = nums2
	else:
		smaller = nums2
		larger = nums1

	if n % 2 == 0:
		return median(smaller[n//2-1:], larger[0:n//2+1])
	else:
		return median(smaller[n//2:], larger[0:n//2+1])
