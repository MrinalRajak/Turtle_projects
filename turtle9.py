# TURTLE PROGRAMS

import turtle
b=turtle.Turtle()
b.color('green')
b.left(90)
b.speed(130)
def tree_bidisha(i):
    if i<10:
        return
    else:
        b.forward(i)
        b.left(30)
        tree_bidisha(3*i/4)
        b.right(60)
        tree_bidisha(3*i/4)
        b.left(30)
        b.backward(i)

tree_bidisha(100)
turtle.done()
        
