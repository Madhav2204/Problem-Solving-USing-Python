# Exercise 3: Area of a Room
# (Solved—13 Lines)
# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.
print("----------------Area of Room Calculator---------------------")
length = float(input("Enter the length of the Room in meters : "))
width = float(input("Enter the width of the Room in meters : "))

areaOfRoom = length * width

print(f"The Area of Room with length {length} meters and width {width} meters is {areaOfRoom} meters")



