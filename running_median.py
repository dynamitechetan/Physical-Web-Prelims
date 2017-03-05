"""
Chetan Kaushik ( dynamitechetan@gmail.com | github.com/DynamiteChetan )
"""

def running_median(user_lst):
	length = len(user_lst)

	if length % 2 == 0:
		# calculates median when number of elements in the list are even
		print ((user_lst[(length // 2) - 1] + user_lst[length//2]) / 2)

	else: 
		# calculates median when number of elements in the list are odd
		print (user_lst[(length - 1 ) // 2] * 1.0 )


if __name__ == "__main__":
	import sys
    # For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
	if sys.version_info.major < 3:
		input_function = raw_input
	else:
		input_function = input
	# input total number of test cases
	number_of_elements = int(input_function().strip()) 
	# initialise empty array
	user_lst = [] 
	# loop to take input and calculate median.
	for i in range(number_of_elements):
		user_lst.append(float(input_function().strip()))
		new_median =  running_median(user_lst)

