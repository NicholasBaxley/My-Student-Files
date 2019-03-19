# CTI-110
# P3HW2 - MealTipTax
# Nicholas Baxley 
# 3/2/19

#Input Meal Charge.
#Input Tip, if tip is not 15%,18%,20%, Display error.
#Calculate tip and 7% sales tax.
#Display tip,tax, and total.


#Ask for Meal Cost
mealcost = int(input("How much did the meal cost? "))

#Ask for Tip
tip = int(input('How much would you like to tip, 15%, 18%, or 20%? '))

#Determines the cost of the meal
if tip == 15 or tip == 18 or tip == 20:
    tipcost = tip * .1
    taxcost = mealcost * .07
    totalcost = mealcost + tipcost + taxcost
    print('The tip cost is', format(tipcost, '4.2f'), '$')
    print('The tax cost is', format(taxcost, '4.2f'), '$')
    print('The total cost is ',format(totalcost, '4.2f'), '$')

#If the amount isnt 15,18,20 it sends back 'Error'
else:
    print('Error')


    

 


























    




