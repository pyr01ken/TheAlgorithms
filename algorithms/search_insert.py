numbers = [1, 3, 5, 6]

def search_insert(array, val):
    low = 0
    high = len(array) - 1
    mid = (low + high) // 2

    while low <= high:
        if array[mid] < val:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid

    return low

print(search_insert(numbers, 7))