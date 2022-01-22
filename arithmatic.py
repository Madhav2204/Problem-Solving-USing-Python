# Exercise 10: Arithmetic
# (Solved—20 Lines)
# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab
import math 
a = int(input("Enter number a = "))
b = int(input("Enter number b = "))

sum = a+b
diff = b-a
product = a*b
quotient = a/b
remainder = a%b
log10 = math.log10(a)
power = math.pow(a, b)
print(f"The Sum of a & b is {sum} \nThe difference when b is substracted from a is {diff}\nThe Product of a & b is {product}")
print(f"the quotient when a/b is {quotient} \nThe Remainder when a/b is {remainder} \nThe  log base 10 of a is {log10} \nThe a raise to power b is {power}")