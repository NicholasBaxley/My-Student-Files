import turtle
window = turtle.Screen()
sf = turtle.Turtle()
sf.color("blue")
sf.speed(0)

for i in range(6):
    sf.forward(100)
    
    for i in range(1):
        sf.left(90)
        sf.forward(40)
        sf.right(90)
        sf.forward(2)
        sf.right(90)
        sf.forward(40)
        for i in range (2):
            sf.left(135)
            sf.forward(40)
            sf.right(90)
            sf.forward(2)
            sf.right(90)
            sf.forward(40)
        
    sf.left(120)
sf.ht()
    
