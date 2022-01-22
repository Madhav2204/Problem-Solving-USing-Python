# Exercise 4: Area of a Field
# (Solved—15 Lines)
# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

print("-----------------Area Of Field Calculator-------------------")
length = float(input("Enter the lenght of Field in feet : "))
width = float(input("Enter the width of Field in feet : "))

areaInFeet = length * width

areaInAcres = areaInFeet/43560

print(f"The area of field with lenght {length} feet and width {width} feet is {areaInFeet} and in Acres {areaInAcres} Acres")