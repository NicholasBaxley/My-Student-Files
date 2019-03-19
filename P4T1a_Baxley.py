import turtle
wn = turtle.Screen()


alex = turtle.Turtle()  #Make alex
wn.bgcolor("black")
alex.color("lightblue")

tess = turtle.Turtle()  #Make tess
tess.color("red")
tess.ht()


for i in range(4):      #alex start
    alex.forward(70)
    alex.left(90)
alex.ht()               #alex finish

tess.st()               #tess start
for i in range(3):      
    tess.left(120)
    tess.forward(70)
tess.ht()               #tess finish
                        
