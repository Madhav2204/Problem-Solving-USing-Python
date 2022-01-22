# Exercise 11: Fuel Efficiency
# (13 Lines)
# In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG). 
# In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPG to L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.

amerricanUnits = int(input("Enter fuel efficiency in miles-pergallon(MPG) : "))
candUnits = amerricanUnits/100
print("The Fuel Efficiency in Canadian Units is ", candUnits)

