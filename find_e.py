'''
Find E to the Nth Digit - 
Enter a number and have the program generate E up to that many decimal places. 
Keep a limit to how far the program will go.
'''

#import the math

import math

def find_e(n):
	print(format(math.e,'.{}f'.format(n)))

#---------------------TEST-------------------

find_e(6)	
find_e(4)
find_e(2)
