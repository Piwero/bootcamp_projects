'''
Next Prime Number - 
Have the program find prime numbers until the user chooses to stop asking for the next one.
'''


def prime_fact():
	prime_list = []
	n = 1
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