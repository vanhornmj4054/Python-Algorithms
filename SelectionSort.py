a = [4,8,2,5,3,1,7,0,6]

def selectionSort(a):
	for i in range(len(a)-1, 0, -1):
		smallest = 0
		for j in range(1, i+1):
			if a[j] > a[smallest]:
				smallest = j
		a[i], a[smallest] = a[smallest], a[i]
	return a

print(selectionSort(a))




