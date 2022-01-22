# Exercise 16: Area and Volume
# (15 Lines)
# Write a program that begins by reading a radius, r, from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r. Use the pi constant in the math module in your
# calculations.
# Hint: The area of a circle is computed using the formula area = πr 2. The
# volume of a sphere is computed using the formula volume = 4
# 3πr 3

import math

radius = float(input("Enter the radius of the circle : "))

areaOfCircle = math.pi*radius**2
volumeOfCircle = (4/3)*math.pi*radius**3

print("The area of Circle is : ", areaOfCircle)
print("The volume of circle is : ",volumeOfCircle)