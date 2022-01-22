# Exercise 5: Bottle Deposits
# (Solved—15 Lines)
# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.

lessThan = int(input("Enter the number of drink containers holding one liter or less  : "))
moreThan = int(input("Enter the number of drink containers holding more than one liter  : "))

totalFromLess = lessThan*0.10 
totalFromMore = moreThan*0.25

totalDeposite = totalFromLess + totalFromMore
print(f"The deposit from drink containers holding one liter or less is {totalFromLess} and deposit from drink containers holding more than one liter is {totalFromMore} ")
print("The total deposit is $ %.2f."%totalDeposite)