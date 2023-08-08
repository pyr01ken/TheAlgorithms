"""
Linear(Sequential) Search => O(n) 
"""

def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
        
    return None

print(linear_search([1, 22, 31, 43, 65, 124, 203], 43))
