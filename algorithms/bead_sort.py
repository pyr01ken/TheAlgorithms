numbers = [54, 2, 9, 12, 1, 234, 7, 12]

def bead_sort(sequence):    

    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("sequence most be list of non-nagtive integers.")
    

    for _ in range(len(sequence)):
        for i, (roud_upper, roud_lower) in enumerate(zip(sequence, sequence[1:])):
            if roud_upper > roud_lower:
                sequence[i] -= roud_upper - roud_lower
                sequence[i+1] += roud_upper - roud_lower


    return sequence


print(bead_sort(numbers))
            