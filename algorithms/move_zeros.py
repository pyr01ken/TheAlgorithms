from typing import List

sequence = [False, 1, 2, 0, 'jack', 0, 0, '123']

def move_zeros(sequence: List):
    zearos = 0
    result = []

    for i in sequence:
        if i == 0 and type(i) == int:
            zearos += 1
        else:
            result.append(i)
    
    result.extend([0] * zearos)

    return sequence, zearos, result
    
print(move_zeros(sequence))
