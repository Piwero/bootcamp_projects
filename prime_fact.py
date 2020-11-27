'''
Prime Factorization - 
Have the user enter a number and find all Prime Factors (if there are any) and display them.
'''


def prime_fact(n):
	prime_list = []
	for item in range(2,(n+1)):
		counter = 0 
		while n%item == 0:
			n = n/item
			counter+=1
		if counter> 0:
			for i in range(counter):
				prime_list.append(item)
			if n ==1:
				print(prime_list)

	
prime_fact(8)










