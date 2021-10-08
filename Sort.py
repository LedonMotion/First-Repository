import random
import time

# insertionSort   插入排序
def insertionSort(array):
	for x in range(1, len(array)):
		key = array[x]
		y = x-1

		while y >= 0 and array[y] > key:
			array[y+1] = array[y]
			y -= 1

		array[y+1] = key


# quickSort   快速排序
def quickSort(array):

	if  len(array) <= 1:
		return array

	left, right = [], []
	middle = array[len(array) // 2]
	array.remove(middle)

	for data in array:
		if data > middle:
			right.append(data)
		else:
			left.append(data)

	return quickSort(left) + [middle] + quickSort(right)


# shellSort   希尔排序
def shellSort(array):

	counter = array[-1]
	length = len(array[:-1])
	gap = length // 2

	while gap > 0:
		for x in range(length):
			y = x
			while (y+gap) < length:
				if array[y] > array[y+gap]:
					array[y], array[y+gap] = array[y+gap], array[y]
				y += gap
				counter += 1
		gap -= 1

	array[-1] = counter



# mergeSort   归并排序
def mergeSort(array):
	if len(array) <= 1:
		return array

	middle = len(array) // 2
	left, right = mergeSort(array[:middle]), mergeSort(array[middle:])
	merge(left+right)

def merge(array):

	length = len(array)
	middle = length // 2



def sortSucc(array):
	index = []
	for x in range(len(array)-1):
		if array[x] < array[x+1]:
			continue
		else:
			index.append(x)
	return index

if __name__ == '__main__':
	array = [x for x in range(1000)]
	random.shuffle(array)
	array.append(0)
	print(array)
	# array = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
	# print(array)
	# new_array = quickSort(array)
	time1 = time.time()
	shellSort(array)
	print(array)
	index = sortSucc(array)
	print(time.time() - time1)
	print(index)
