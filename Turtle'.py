#Turtle
import turtle
hr=turtle.Turtle()
hr.left(90)
hr.color("red","black")
hr.speed(150)
def tree(i):
     if i<5:
         return
     else:
        hr.forward(i)
        hr.left(30)
        tree(3*i/4)
        hr.right(60)
        tree(3*i/4)
        hr.left(30)
        hr.backward(i)
tree(70)
turtle.done()
     
