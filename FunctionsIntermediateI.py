import random
def randInt(min=0, max=100):
	if min > max:
		return "Min is greater than max"
	return round(random.random() * (max - min) + min) 

print(randInt())
print(randInt(max = 500))
print(randInt(min = 50))
print(randInt(min = 50, max = 500))
print(randInt(min = -500, max = -50))
print(randInt(min = 500, max = 50))




