'''
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
'''


def fib_sequence(num):
	fibonacci_list = [0,1]
	repeat_list = 1
	statement = True

	while statement:
		new_number = fibonacci_list[-1]+ fibonacci_list[-2]
		fibonacci_list.append(new_number)
		if len(fibonacci_list) == num:
			break

	print(fibonacci_list)

#--------------test----------------

fib_sequence(80)




