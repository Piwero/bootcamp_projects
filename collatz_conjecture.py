
'''
Collatz Conjecture
Start with a number n > 1. 
Find the number of steps it takes to reach 1 using the following process: 
If n is even, divide it by 2. 
If n is odd, multiply it by 3 and add 1.
'''

#dif if even or odd

def collatz(number):
	n = number
	while n > 1:
		if number % 2 == 0:
			n = (number/3) +1
			print(n)

		else:
			n = (number/2)
			print(n)

collatz(5)

#add each rule for even or odd

#count steps (creating a list?)
