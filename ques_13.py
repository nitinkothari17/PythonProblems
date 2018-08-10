first = 0 
second = 1
for i in range(2,100):
	last_element = first + second
	first = second
	second = last_element
print last_element
