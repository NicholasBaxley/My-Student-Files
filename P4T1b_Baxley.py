import turtle
window = turtle.Screen()
window.bgcolor("black")


letterN = turtle.Turtle()   #Letter N's properties
letterN.pensize(4)
letterN.color("red")

letterN.left(90)            #Letter N's Movement
letterN.forward(50)
letterN.right(154)
letterN.forward(56)
letterN.left(154)
letterN.forward(50)
letterN.ht()


letterB = turtle.Turtle()   #Letter B's properties
letterB.pensize(4)
letterB.color("red")

letterB.penup()             #Letter B's Movement 
letterB.forward(40)
letterB.pendown()
letterB.left(90)
letterB.forward(50)
letterB.right(90)
letterB.speed(0)
for i in range(50):
    letterB.forward(.8)
    letterB.right(3.6)
letterB.right(180)
letterB.forward(5)
for i in range(50):
    letterB.forward(.8)
    letterB.right(3.6)
letterB.forward(5)
letterB.ht()
