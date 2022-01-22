# Exercise 8:Widgets and Gizmos
# (15 Lines)
# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

widgetsNumber = int(input("Enter the number of widgets : "))
gizmosNumber = int(input("Enter the number of Gizmos : "))

widgetsWeighs = 75
gizmos = 112

totalWeigh = widgetsNumber*widgetsWeighs + gizmos*gizmosNumber

print(f"The total weigh of widgets and gizmos is {totalWeigh} grams")