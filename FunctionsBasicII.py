def countdown(num):
	newList = []
	for i in range(num, -1, -1):
		newList.append(i)
	print newList
	return newList

countdown(5)

def printAndReturn(list):
	print list[0]
	return list[1]

print printAndReturn([1,2])

def firstPlusLength(list):
	return (list[0] + len(list))

print firstPlusLength([1,2,3,4])

def valuesGreaterThanSecond(list):
	newList = []
	count = 0
	for i in list:
		if len(list) < 2:
			return False
		elif i > list[1]:
			count += 1
			newList.append(i)
	print count
	return newList

print valuesGreaterThanSecond([5,2,3,2,1,4])
print valuesGreaterThanSecond([3])

def thisLengthThatValue(size,value):
	newList = []
	for i in range(0, size, 1):
		newList.append(value)
	return newList

print thisLengthThatValue(4,7)
print thisLengthThatValue(6,2)






