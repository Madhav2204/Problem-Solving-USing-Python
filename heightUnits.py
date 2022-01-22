# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.

inchPerFeet = 12
cmPerInch = 2.54
numberOfFeets = int(input("Enter your height in feets : "))
numberOfInches = int(input("Enter your height in Inches : "))

eqCentimeters = (numberOfFeets * inchPerFeet + numberOfInches) * cmPerInch

print(f"Your Height in Centimeters is : {eqCentimeters} ")