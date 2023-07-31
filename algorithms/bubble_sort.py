numbers = [10, 23, 4, 345, 21, 98, 8]

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

print(bubble_sort(numbers))
