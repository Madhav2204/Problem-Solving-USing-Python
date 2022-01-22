# Exercise 19: Free Fall
# (Solved—16 Lines)
# Create a program that determines how quickly an object is traveling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
# due to gravity is 9.8 m/s2. You can use the formula vf =
# 
# v2
# i + 2ad to compute the
# final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.

from math import sqrt

gravity = 9.8

d = float((input("Height from which the object is dropped(in meters) :")))
vf = sqrt((2*gravity*d))

print(f"It will hit the ground at {vf} m/s")