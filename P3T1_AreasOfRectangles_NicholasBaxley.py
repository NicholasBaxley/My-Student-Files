# CTI-110
# P3HW1 - Color Mixer
# Nicholas Baxley 
# 3/1/19

#Gets the width and length of both rectangles
length1 = int(input("What is the length of the first rectangle? "))
width1 = int(input("What is the width of the first rectangle? "))

length2 = int(input("What is the length of the second rectangle? "))
width2 = int(input("What is the width of the second rectangel? "))

#Determines the area of each rectangle
area1 = length1 * width1
area2 = length2 * width2

#Outputs the result

if area1 > area2:
    print("The first rectangle is bigger.")

elif area2 > area1:
    print("The second rectangle is bigger.")

else:
    print("They are the same size.")
    

 

