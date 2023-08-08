def search_range(nums, target):
    low = 0
    high = len(nums)- 1

    while low <= high:
        mid = low + (high - low) // 2
        if target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            break
    
    for i in range(len(nums)-1 , -1, -1):
        if target == nums[i]:
            return [mid, i]

    return [None, None]

print(search_range([1, 2, 2, 3, 4, 5, 6, 6, 6, 7], 2))