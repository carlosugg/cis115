# CIS 115
# grauc
# M3T2
# 10/3/18

# Turtle python example 2

import turtle

def main():
    alex = turtle.turtle()
    bob = turtle.turtle()
    christine = turtle.turtle()

    
    # customize the turtles
    alex.pensize(3)
    bob.pensize(4)
    christine.pensize(2)
    alex.pencolor("red")
    bob.pencolor("green")
    christine.pencolor("blue")

    sides = int(input("Number of sides? ")
    size = int(input("Size of polygon? ")
    drawPolygon(alex, sides, size)
               
    # draw shapes
    drawPolygon(alex, sides, size)
    drawPolygon(bob, sides, size)
    drawPolygon(christine, sides, size)


def drawpolygon(t, sides, size):
    """
    uses turtle to draw a n sided polygon
    input: t - a turtle
           sides - number of sides
           size - lenght of one side

    """
    for side in range(sides)
        t.forward(size)
        t.right(360/sides) # angle depends on polygon

# run program
main()

    
