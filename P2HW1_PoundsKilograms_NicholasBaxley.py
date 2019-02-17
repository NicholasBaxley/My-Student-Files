# The program will convert Pounds into Kilograms
# 2/16/2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Nicholas Baxley


#Gets the number of pounds
pounds = float(input('Input the amount of pounds. '))

#Converts it into kilograms
kilo = pounds / 2.2046

#Presents the amount of kilograms in a legible way
print('Kilograms=',format(kilo ,'.2f'))
