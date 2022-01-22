# Exercise 18:Volume of a Cylinder
# (15 Lines)
# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place
import math
radius = float(input("Enter the radius of base of a Cylinder : "))
height = float(input("Enter the height of the cylinder : "))

areaOfCircularBase = (math.pi)*radius**2
volumeOfCylinder = areaOfCircularBase * height
print("Volume of Cylinder is : ", volumeOfCylinder)