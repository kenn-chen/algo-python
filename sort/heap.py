def sort(nums):
    parent = lambda x: (x-1)//2
    n = len(nums)
    for i in range(parent(n-1), -1, -1):
        _heapify(nums, n, i)
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        _heapify(nums, i, 0)

def _heapify(nums, n, i):
    max_num = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and nums[max_num] < nums[l]:
        max_num = l
    if r < n and nums[max_num] < nums[r]:
        max_num = r
    if max_num != i:
        nums[i], nums[max_num] = nums[max_num], nums[i]
        _heapify(nums, n, max_num)
