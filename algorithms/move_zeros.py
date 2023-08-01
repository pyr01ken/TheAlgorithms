from typing import List

sequence = [False, 1, 2, 0, 'jack', 0, 0, '123']

def move_zeros(sequence: List):
    zearos = 0
    lst = []

    for i in sequence:
        if i == 0 and type(i) == int:
            zearos += 1
        else:
            lst.append(i)
    
    lst.extend([0] * zearos)

    return sequence, zearos, lst
    
print(move_zeros(sequence))
