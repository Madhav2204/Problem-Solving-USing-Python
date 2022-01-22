# Exercise 7: Sum of the First n Positive Integers
# (Solved—12 Lines)
# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = (n)(n + 1)/2

num = int(input("Enter a positive interger : "))

sum = ((num+1)*num)/2

print(f"The sum of first {num} Positive integers is : {sum}")
