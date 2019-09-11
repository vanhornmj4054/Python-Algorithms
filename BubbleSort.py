# a = [4,8,2,5,3,1,7,0,6]

# def sort(a):
# 	for i in range(len(a)-1, 0, -1):
# 		for j in range(i):
# 			if a[j] < a[j+1]:
# 				a[j], a[j+1] = a[j+1], a[j]
# 	print(a)

# sort(a)


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




