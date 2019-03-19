# CTI-110
# P3HW1 - Color Mixer
# Nicholas Baxley
# 3/1/19

#Pseudocode

#Input number 1-10.
#Display error if not 1-10.
#Calculate the roman numeral for inputted number.
#Display roman numeral.


#Code

#Ask for input.
number = int(input("Input a number 1-10. "))

#If the number is bigger than 10 send error.
if number > 10:
    print("Error: value to big!")
    
#If the number is smaller than 1 send error.
elif number < 1:
    print("Error: value to small!")

#Send the correct response back depending on input.
else:
    if number == 1:
        print("I")

    elif number == 2:
        print("II")

    elif number == 3:
        print("III")

    elif number == 4:
        print("IV")

    elif number == 5:
        print("V")

    elif number == 6:
        print("VI")

    elif number == 7:
        print("VII")

    elif number == 8:
        print("VIII")

    elif number == 9:
        print("IX")

    elif number == 10:
        print("X")
        
    
    





