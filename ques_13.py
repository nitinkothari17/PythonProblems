"""Q13
Here's another one (12th was too easy)
1. Write a recursive function to return 100th fibonacci number.
2. Optimize the function to reduce execution time. """

first = 0 
second = 1
for i in range(2,100):
	last_element = first + second
	first = second
	second = last_element
print last_element
