"""This function returns the maximum and 
minimum numbers in a given array"""

def max_min(numberList):
	output =[]
	
	if max(numberList) == min(numberList):
		output.append(max(numberList))

	else:
		output.append(min(numberList))
		output.append(max(numberList))

	return output

#print max_min([1,2,3,4])
#print max_min([6,4])
#print max_min([4,4,4,4,])

