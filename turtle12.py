# TURTLE programs

import turtle

m=turtle.Turtle()
m.pensize()
m.speed(150)
m.color('black')
m.shape()
m.left(90)
m.penup()
m.forward(100)
m.left(90)
m.forward(250)
m.right(90)
m.backward(250)
m.pendown()
m.forward(400)
m.backward(400)
m.right(90)
m.forward(400)
m.backward(400)
m.left(49)
m.penup()
m.forward(200)
m.color('green')
m.pendown()
for i in range(500):
    m.right(3)
    m.forward(i/100.)

    i=i+1
    


