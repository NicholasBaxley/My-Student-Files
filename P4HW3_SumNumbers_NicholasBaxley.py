# Adding up mutiple numbers
# 3/18/2019
# CTI-110 P4HW3 - Sum of Numbers
# Nicholas Baxley

#Input number
#If negative end program
#Ask to input more
#If no more numbers, add up the sum
#Print the sum

answer = str("y")
total = 0
while answer == str("y"):
    number = int(input("Please input a number. "))
    if number > 0:
        total += number
        answer = input("Do you want to add another number, y or n? ")

        if answer == str("n"):
            print("This is your total: ", format(total, "4.2f"))

        if answer != str("y") and answer != str("n"):
            print("Not valid")
        
    else:
        print("Invalid amount, please input correct amount next time.")
        answer = 20



    
    
    

