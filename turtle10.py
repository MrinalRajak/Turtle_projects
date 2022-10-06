# TURTLE PROGRAM

import turtle
m=turtle.Turtle()
m.speed(250)
m.pensize(2)
m.shape()
for i in range(260):
    
    m.right(52)
    m.color('red')
    m.forward(i**2/1000)
    i=i+1
m.left(90)
for i in range(10):
    m.left(4)
    m.pensize(10)
    m.color('green')
    m.forward(20)
    i=i+1
    
m.left(180)
m.forward(50)
m.right(45)
m.forward(30)
m.right(180)
m.forward(20)
m.right(50)
m.forward(20)
m.right(90)
m.penup()
m.forward(50)
m.right(90)
m.forward(20)
m.left(90)
m.pendown()
for i in range(8):
    m.left(10)
    m.forward(10)
    i=i+1

m.right(90)
m.penup()
m.forward(50)
m.right(120)
m.forward(93)
m.left(45)
m.pendown()
m.right(5)
m.forward(13)





























    


