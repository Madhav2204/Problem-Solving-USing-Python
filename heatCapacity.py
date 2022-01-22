# Exercise 17: Heat Capacity
# (Solved—25 Lines)
# The amount of energy required to increase the temperature of one gram of a material
# by one degree Celsius is the material’s specific heat capacity, C. The total amount
# of energy required to raise m grams of a material by ΔT degrees Celsius can be
# computed using the formula:
# q = mCΔT.
# Write a program that reads the mass of some water and the temperature change
# from the user. Your program should display the total amount of energy that must be
# added or removed to achieve the desired temperature change.
# Hint: The specific heat capacity of water is 4.186 J
# g◦C. Because water has a density of 1.0 gram per millilitre, you can use grams and millilitres interchangeably
# in this exercise.
# Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this
# exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
# your program to compute the cost of boiling water for a cup of coffee.
# Hint: You will need to look up the factor for converting between Joules and
# kilowatt hours to complete the last part of this exercise.

heatCapacityOfWater = 4.186
priceOfElectricity = 8.9
JToKWH = 2.777e-7

#input from user
volume = float(input("Enter the amount of water in millimeters : "))
d_temp = float(input("Enter the temparature increase (Degree celcius) : "))

q = volume * d_temp * heatCapacityOfWater

print(f"We Will require {q} joules of Energy")

kwh = q*JToKWH
cost = kwh*priceOfElectricity

print(f"That much Energy will Cost {cost} cents ")
