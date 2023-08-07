"""
remove min
 [4, 2, 1, -2, 9, 5] => -2
"""

def remove_min(stack):
    storeage_stack = []
    if len(stack) == 0:
        return stack
    
    min = stack.pop()
    stack.append(min)
    for i in range(len(stack)):
        val = stack.pop()
        if val <= min:
            min = val
        storeage_stack.append(val)
    
    for i in range(len(storeage_stack)):
        val = storeage_stack.pop()
        if val != min:
            stack.append(val)

    return stack, min

print(remove_min([4, 2, 1, -2, 9, 5]))
