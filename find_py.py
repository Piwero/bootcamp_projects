'''
Find PI to the Nth Digit - 
Enter a number and have the program generate PI up to that many decimal places. 
Keep a limit to how far the program will go.
'''

#import the math

import math

def find_pi(n):
	print(format(math.pi,'.{}f'.format(n)))

#---------------------TEST-------------------

find_pi(6)	
find_pi(4)
find_pi(2)
