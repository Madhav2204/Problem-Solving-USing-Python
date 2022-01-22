# Exercise 6: Tax and Tip
# (Solved—17 Lines)
# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

taxRate = 0.05
tipRate =   0.18

costOfMeal = float(input("Enter the Cost of Meal ordered : "))

taxAmount = costOfMeal*taxRate
tipAmount = costOfMeal*tipRate

totalAmount = costOfMeal+ taxAmount + tipAmount

print("The Total tax amount is = %.2f\nTotal tip amount is = %.2f\nTotal payable amount is = %.2f"%(taxAmount,tipAmount,totalAmount))
