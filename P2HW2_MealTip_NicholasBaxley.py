# Calculating a meal and the tip amounts.
# 2/16/2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Nicholas Baxley



#Gets the cost of the base meal
foodCost = float(input('How much did your food cost? '))


#Calculates the tip amounts
tip15 = foodCost * .15
tip18 = foodCost * .18
tip20 = foodCost * .20


#Prints out the tip and total cost of each tip amount
print('A 15% tip is',format(tip15, '.2f',),'and the total cost is',foodCost + tip15)
print('A 18% tip is',format(tip18, '.2f',),'and the total cost is',foodCost + tip18)
print('A 20% tip is',format(tip20, '.2f',),'and the total cost is',foodCost + tip20)
