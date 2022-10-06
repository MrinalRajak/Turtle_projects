#Turtle
import turtle
import numpy as np
tu=turtle.Turtle()
tu.screen.bgcolor("black")
tu.pensize(2)
tu.color("brown")
tu.left(90)
tu.backward(100)
tu.shape('turtle')
tu.speed(500)
def tree(i):
     if i<10:
          return
     else:
          tu.forward(i)
          tu.color("green")
          tu.circle(2)
          tu.color("brown")
          tu.left(30)
          tree((np.pi)*i/4)
          tu.right(60)
          tree((np.pi)*i/4)
          tu.left(30)
          tu.backward(i)
tree(100)
turtle.done()
     
