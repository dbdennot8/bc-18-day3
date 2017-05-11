"""This function returns the maximum and 
minimum numbers in a given array"""

def max_min(number_list):
	output =[]
	
	if max(number_list) == min(number_list):
		output.append(max(number_list))

	else:
		output.append(min(number_list))
		output.append(max(number_list))

	return output

#print max_min([1,2,3,4])
#print max_min([6,4])
#print max_min([4,4,4,4,])

