# Exercise 13: Making Change
# (Solved—33 Lines)
# Consider the software that runs on a self-checkout machine. One task that it must be
# able to perform is to determine how much change to provide when the shopper pays
# for a purchase with cash.
# Write a program that begins by reading a number of cents from the user as an
# integer. Then your program should compute and display the denominations of the
# coins that should be used to give that amount of change to the shopper. The change
# should be given using as few coins as possible. Assume that the machine is loaded
# with pennies, nickels, dimes, quarters, loonies and toonies.
# A one dollar coin was introduced in Canada in 1987. It is referred to as a
# loonie because one side of the coin has a loon (a type of bird) on it. The two
# dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is
# derived from the combination of the number two and the name of the loonie.

centsPerToonie = 200
centsPerLoonie = 100
centsPerQuarter = 25
centsPerDime  = 10
centsPerNickel = 5
numberOfCents = int(input("Enter The Number of Cents : "))

#to compute number of toonies by performing an integer division by 200, then compute the amount of change that still needs to be considered by computing the remainder after dividing by 200

print(' ', numberOfCents//centsPerToonie , 'toonies')
numberOfCents = numberOfCents%centsPerToonie

#same for all
print(' ', numberOfCents//centsPerLoonie , 'loonies')
numberOfCents = numberOfCents%centsPerLoonie

print(' ', numberOfCents//centsPerQuarter , 'quarters')
numberOfCents = numberOfCents%centsPerQuarter

print(' ', numberOfCents//centsPerDime , 'dimes')
numberOfCents = numberOfCents%centsPerDime

print(' ', numberOfCents//centsPerNickel , 'nickels')
numberOfCents = numberOfCents%centsPerNickel

# display the number of pennies
print(' ',numberOfCents,'pennies')




