"""
Chetan Kaushik ( dynamitechetan@gmail.com | github.com/DynamiteChetan )
"""

class Queue(object):

	def __init__(self):
		self.q = []

	#put element at the end
	def put(self, element):
		self.q.append(element)

	#pop first element (FIFO)
	def pop(self):
		self.q.pop(0)

	#get first element
	def peek(self):
		return self.q[0]

def test(input_function,queue,inp):
		if inp[0] == 1:
			# Enter element in end of the queue
			queue.put(inp[1]) 

		elif inp[0] == 2:
			# Remove element from queue front.
			queue.pop()

		elif inp[0] == 3:
			# Print the front element of queye.
			first_ele = queue.peek()
			print(first_ele)
		else:
			print("1 x: Enqueue element x into the end of the queue.\n2: Dequeue the element at the front of the queue.\n3: Print the element at the front of the queue.")
			exit()

if __name__ == "__main__":
	import sys
    # For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
	if sys.version_info.major < 3:
		input_function = raw_input
	else:
		input_function = input

	# declaration of Queue
	queue = Queue()
	# input total test cases
	total_test_cases = int(input_function())
	for i in range(total_test_cases):
		# taking input from user about next operation
		inp = list(map(int, input_function().strip().split(' ')))
		# calling function to run queue operations
		test(input_function,queue,inp)
	# delete queue to free memory.
	del queue