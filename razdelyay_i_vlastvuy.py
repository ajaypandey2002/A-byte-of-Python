def max(arr):
	total = 0
	for x in arr:
		if x >= total:
			total = x
	return total

print(max([1, 6, 3, 4]))

def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]
		return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

