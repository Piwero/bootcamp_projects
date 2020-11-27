'''
Mortgage Calculator - 
Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
Also figure out how long it will take the user to pay back the loan. 
For added complexity, add an option for users to select the compounding interval 
(Monthly, Weekly, Daily, Continually).
'''



def mortgage_calculator():
	mortgage = float(input("Enter mortgage amount in £ : "))
	compounding = input("Select Monthly = 'M', Weekly= 'W', Daily= 'D' : ")
	terms = int(input("How many years : "))
	interest = float(input("Enter interest rate: "))
	interest = interest/100
	
	mortgage_with_interest = mortgage +mortgage*interest
	if compounding == 'M':
		terms = terms*12
	elif compounding == 'W':
		terms = terms*52

	elif compounding == 'D':
		terms = terms*360

	else:
		print('Pleaser enter a correct compounding')
		mortgage_calculator()

	value_per_payment = round(mortgage_with_interest/terms,2)
	repayments= mortgage_with_interest/value_per_payment
	print("you will pay £{} per {} for {} payments which make a total of £{}".format(value_per_payment,compounding,repayments,mortgage_with_interest))


mortgage_calculator()



