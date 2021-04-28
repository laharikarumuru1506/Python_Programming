import turtle

wn = turtle.Screen()
wn.bgcolor("black")
m = turtle.Turtle()

m.speed(0)
m.left(65)
m.color("cyan")
for i in range(0,200,1):
    for x in range(4):
        m.forward(i)
        m.left(98)

    m.left(45)

turtle.done()
