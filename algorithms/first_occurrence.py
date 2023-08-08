
def first_occurrence(array, element):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if low == high:
            break

        if array[mid] < element:
            low = mid + 1
        else:
            high = mid

    if array[low] == element:
        return low


print(first_occurrence([1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 6], 6))
