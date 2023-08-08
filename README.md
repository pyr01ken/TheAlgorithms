# Big-O Notation

![bio-o notation](doc/big-o-notation.png)

## 1. Linear Time O(n)
```python
def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
```

## 2. Logarithm Time O(log n)
```python
def binary_search(array, element):
    low, high = 0, len(array)-1
    while low <= high:
        mid = (high + low) // 2
        val = array[mid]
        if val == element:
            return mid
        elif val < element:
            low = mid + 1
        else:
            high = mid - 1
```

## 3. Polynomial Time O(n^number)
This example for O(n^2)
```python
def bubble_sort(collection):
	length = len(collection)
	for i in range(length - 1):
		swapped = False
		for j in range(length - 1 - i):
			if collection[j] > collection[j+1] :
				swapped = True
				collection[j], collection[j+1] = collection[j+1] , collection[j]
		if not swapped:
			break
	return collection
```
## 4. Exponential Time O(number^n)
This example for O(3^n)
```python
from itertools import chain, combinations
def subsets(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
print(list(sunsets(['a', 'b', 'c'])))
```

## Sort 
- bubble sort
- bead sort

## Cryptograpy 
- ceasar
- a1z26
- one time pad cipher

## Search 
- binary search
- linear search
- search insert
- search range
- first occurrence
- last occurrence
- top one
- two sum

## Other
- zigzag
- move zearos
- limit
- is isomophic
- remove min
- rotate