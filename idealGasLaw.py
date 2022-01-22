# Exercise 20: Ideal Gas Law(19 Lines)
# The ideal gas law is a mathematical approximation of the behavior of gasses as pressure, volume and 
# temperature change. It is usually stated as:
# PV = nRT. where P is the pressure in Pascals, V is the volume in liters, n is the amount of
# substance in moles, R is the ideal gas constant, equal to 8.314 Jmol K , and T is the
# temperature in degrees Kelvin. Write a program that computes the amount of 
# gas in moles when the user supplies the pressure, volume and temperature. 
# Test your program by determining the number of moles of gas in a SCUBA tank. 
# A typical SCUBA tank holds 12 liters of gas at a pressure of 20,000,000 Pascals (approximately 3,000 PSI).
#  Room temperature is approximately 20 degrees Celsius or 68 degrees Fahrenheit.
# Hint: A temperature is converted from Celsius to Kelvin by adding 273.15
# to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it,
# multiply it by 59 and then add 273.15 to it.

R = 8.314 
pressure = float(input("Enter the amount of pressure in pascals : "))
volume = float(input("Enter the volume of gas in liters :"))
temperature = float(input("Enter the temparature in celcius : "))

temperatureInKelvin = 273.15 + temperature
n = R*temperature/pressure*volume
print(f"The amount of sustance in Moles is : {n}")

#result
# Enter the amount of pressure in pascals : 20000000
# Enter the volume of gas in liters :12
# Enter the temparature in celcius : 20
# The amount of sustance in Moles is : 9.9768e-05


