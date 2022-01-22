# Exercise 15: Distance Units
# (20 Lines)
# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized

numberOfFeets = int(input("Enter your measurement in feets : "))

eqDistanceInInches = 12 * numberOfFeets
eqDistanceInYards = numberOfFeets/3.0
eqDistanceInmiles = numberOfFeets/5280.0

print(f"Eqivalent Distance in Inches : {eqDistanceInInches}")
print(f"Eqivalent Distance in Yards : {eqDistanceInYards}")
print(f"Eqivalent Distance in Miles: {eqDistanceInmiles}")