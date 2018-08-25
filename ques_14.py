def swap(tuples,i):
	a = tuples[i]
	tuples[i] = tuples[i+1]
	tuples[i+1] = a
	
tuples = [("Tom",19,80),("John",20,90),("Jony",17,91),("Jony",17,93),("Json",21,85)]
for i in xrange(len(tuples)-1):
	if tuples[i][0] > tuples[i+1][0]:
		swap(tuples,i)
		continue
	if tuples[i][1] > tuples[i+1][1]: 
		swap(tuples,i)
		continue
	if tuples[i][2] > tuples[i+1][2]: 
		swap(tuples,i)
		continue
print tuples
