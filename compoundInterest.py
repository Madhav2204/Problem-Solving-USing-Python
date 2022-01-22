# Exercise 9: Compound Interest
# (19 Lines)
# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

#formula pf CI , Amount = P(1+(r/n))**nt

amountDeposited = int(input("Enter the amount you want to deposite : "))

totalAfterYear = amountDeposited*((1+(4/100))**1)
totalAfterTwoYear = amountDeposited*((1+(4/100))**2)                                          
totalAfterThreeYear = amountDeposited*((1+(4/100))**3) 

print("The amount in your saving account after one year is %.2f"%totalAfterYear)
print("The Amount in Your saving account after Two year is %.2f"%totalAfterTwoYear)
print("The Amount in Your saving account after Three year is %.2f"%totalAfterThreeYear)


