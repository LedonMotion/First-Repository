# lineSearch(array, target)
def lineSearch(array, target):
	for obj in range(len(array)):
		if target == array[obj]:
			return obj

# binarySearch(array, target, start=0, end=None)
def binarySearch(array, target, start=0, end = None):

	if end == None:
		end = len(array)-1
	else:
		end = end
	middle = (start + end) // 2

	if start > end:	
		return -1
	
	if target == array[middle]:
		return middle

	elif target > array[middle]:
		start = middle + 1

	elif target < array[middle]:
		end = middle - 1
	
	return binary(array, target, start, end)


# insertionSearch(array, target)
def insertionSearch(array, target)
	start = 0
	end = len(array)
	middle = (start + end) // 2
	while True:
		if target == array[middle]:
			return middle
		elif target 

if __name__ == '__main__':
	a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
	mid = lineSearch(a, 7)
	print(mid)

	mid = (8-0)*(7-0)/(8-0)
	pri