# CTI-110
# P3HW1 - Color Mixer
# Nicholas Baxley
# 3/1/19


#Input color1 and color2
#If Input is not red,blue, or yellow send error
#Display result of the 2 colors



#Collects the value for the first color
p_color1 = input("Input first color. ")
if p_color1 == "red":
    color1 = 1
else:
    if p_color1 == "blue":
        color1 = 10
    else:
        if p_color1 == "yellow":
            color1 = 22
        else:
            print('Invalid color')
            
#Collects the value for the second color
p_color2 = input("Input the second color. ")
if p_color2 == "red":
    color2 = 1
else:
    if p_color2 == "blue":
        color2 = 10
    else:
        if p_color2 == "yellow":
            color2 = 22
        else:
            print('Invalid color')

#Combines the values and outputs the result
color = color1 + color2

if color == 2:
    print('Red')
elif color == 20:
    print('Blue')
elif color == 44:
    print('Yellow')
elif color == 11:
    print('Purple')
elif color == 23:
    print('Orange')
elif color == 32:
    print('Green')
    

            
    



     
    





   
    
