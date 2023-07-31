numbers = [1, 2, 1, 3, 4, 2]

def top(lst):
    values = {}
    result = []
    f_val = 0

    for i in lst:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    f_val = max(values.values())

    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            continue # why use this?
    
    return result

print(top(numbers))