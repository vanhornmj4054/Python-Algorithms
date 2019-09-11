# def biggieSize(list):
# 	for i in range(0, len(list)):
# 		if list[i] > 0:
# 			list[i] = "big"
# 	return list

# print biggieSize([-1,3,5,-5])

# def countPositives(arr):
# 	count = 0
# 	for i in range(0, len(arr)):
# 		if arr[i] > 0:
# 			count += 1
# 	arr[len(arr)-1] = count
# 	return arr

# print countPositives([-1,1,1,1])
# print countPositives([1,6,-4,-7,-2])

# def sumTotal(list):
# 	return sum(list)

# print sumTotal([1,2,3,4])
# print sumTotal([6,3,-2])

# def average(list):
# 	sum = 0
# 	if len(list) < 1:
# 		return 0
# 	for i in range(0, len(list)):
# 		sum += list[i]
# 	return sum / float(len(list))


# print average([1,2,3,4])
# print average([])

# def length(list):
# 	return len(list)

# print length([37,2,1,-9])
# print length([])

# def minimum(list):
# 	if len(list) < 1:
# 		return False
# 	return min(list)

# print minimum([37, 2, 1, -9])
# print minimum([])

# def maximum(list):
# 	if len(list) < 1:
# 		return False
# 	return max(list)

# print maximum([37,2,1,-9])
# print maximum([])

# def ultimateAnalysis(list):
# 	dict = {'sumTotal': 0,
# 			'average': 0,
# 			'minimum': 0,
# 			'maximum': 0,
# 			'length': 0 
# 			}
# 	avg = 0
# 	if len(list) < 1:
# 		return 0
# 	for i in range(0, len(list)):
# 		avg += list[i]
# 	avg = avg / float(len(list))
# 	dict['sumTotal'] = sum(list)
# 	dict['average'] = avg
# 	dict['minimum'] = min(list)
# 	dict['maximum'] = max(list)
# 	dict['length'] = len(list)
# 	return dict

# print ultimateAnalysis([37,2,1,-9])

# def reverseList(list):
# 	y = len(list) - 1
# 	temp = 0
# 	for i in range(0, len(list)/2):
# 		temp = list[i]
# 		list[i] = list[y]
# 		list[y] = temp
# 		y -= 1
# 	return list

# print reverseList([37,2,1,-9])



