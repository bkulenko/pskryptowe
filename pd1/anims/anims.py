from turtle import RawTurtle
from math import sqrt, atan, degrees, radians, cos, sin


def koch(turtle: RawTurtle, depth):
    edge = 500/1.2
    turtle.penup()
    turtle.setpos(-edge/2, edge*sqrt(3)/6)
    turtle.pendown()
    for _ in range(3):
        __koch_curve(turtle, depth, edge)
        turtle.right(120)
    turtle.teleport(0, 0)


def striangle(turtle: RawTurtle, depth):
    edge = 500/1.2
    turtle.penup()
    turtle.setpos(-edge/2, edge*sqrt(3)/6)
    turtle.pendown()
    __triangle(turtle, depth, edge)
    turtle.teleport(0, 0)


def scarpet(turtle: RawTurtle, depth):
    edge = 500/1.2
    turtle.penup()
    turtle.setpos(-edge/2, edge*sqrt(3)/3)
    turtle.pendown()
    __carpet(turtle, depth, edge)
    turtle.teleport(0, 0)


def peano(turtle: RawTurtle, depth):

    edge = 500/sqrt(2)
    turtle.penup()
    turtle.setpos(-edge/sqrt(2), 0)
    turtle.pendown()
    __peano(turtle, depth, edge)
    turtle.teleport(0, 0)


def dragon(turtle: RawTurtle, depth):
    edge = 500/2
    turtle.penup()
    turtle.setpos(-edge/2.3, 0)
    turtle.pendown()
    __dragon(turtle, depth*3, edge)
    turtle.teleport(0, 0)


def btree(turtle: RawTurtle, depth):

    turtle.left(90)
    edge = 500/3
    turtle.penup()
    turtle.setpos(-edge/5, -edge/5)
    turtle.pendown()
    __btree(turtle, depth*3, edge/1.2)
    turtle.teleport(0, 0)
    turtle.right(90)


def ptree_base(turtle: RawTurtle, depth):

    turtle.left(90)
    edge = 500/3
    turtle.penup()
    turtle.setpos(edge/2, 0)
    turtle.pendown()
    __ptree_base(turtle, depth*3, edge/2)
    turtle.teleport(0, 0)
    turtle.right(90)


def ptree_mod(turtle: RawTurtle, depth):

    turtle.left(90)
    edge = 500/3
    turtle.penup()
    turtle.setpos(edge/2, -edge/2)
    turtle.pendown()
    __ptree_mod(turtle, depth*3, edge/2, 30)
    turtle.teleport(0, 0)
    turtle.right(90)


def ptree_notrunk(turtle: RawTurtle, depth):

    turtle.left(90)
    edge = 500/3
    turtle.penup()
    turtle.setpos(edge/2, 0)
    turtle.pendown()
    __ptree_notrunk(turtle, depth*2, edge/3, 40)
    turtle.teleport(0, 0)
    turtle.right(90)


def ptree_tilt(turtle: RawTurtle, depth):

    turtle.left(90)
    edge = 500/4
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.pendown()
    __ptree_tilt(turtle, depth*2, edge/3)
    turtle.teleport(0, 0)
    turtle.right(90)


def __koch_curve(turtle: RawTurtle, n, d):
    if not n:
        turtle.forward(d)
        return
    __koch_curve(turtle, n-1, d/3)
    turtle.left(60)
    __koch_curve(turtle, n-1, d/3)
    turtle.right(120)
    __koch_curve(turtle, n-1, d/3)
    turtle.left(60)
    __koch_curve(turtle, n-1, d/3)


def __triangle(turtle: RawTurtle, n, d):
    turtle.color(255, 0, 0)

    def triangle(turtle: RawTurtle, d):
        for _ in range(3):
            turtle.forward(d)
            turtle.right(120)
        return
    if not n:
        triangle(turtle, d)
        return
    for _ in range(3):
        __triangle(turtle, n-1, d/2)
        turtle.forward(d)
        turtle.right(120)


def __carpet(turtle: RawTurtle, n, d):
    turtle.color(255, 0, 0)

    def __square(turtle: RawTurtle, d):
        for _ in range(4):
            turtle.forward(d)
            turtle.right(90)

    if not n:
        __square(turtle, d)
        return

    for _ in range(4):
        for _ in range(2):
            __carpet(turtle, n-1, d/3)
            turtle.forward(d/3)
        turtle.forward(d/3)
        turtle.right(90)


def __peano(turtle, n, d):
    if not n:
        turtle.forward(d*sqrt(2))
        return
    __peano(turtle, n-1, d/3)
    turtle.left(90)
    for _ in range(3):
        __peano(turtle, n-1, d/3)
        turtle.right(90)
    for _ in range(3):
        __peano(turtle, n-1, d/3)
        turtle.left(90)
    __peano(turtle, n-1, d/3)
    turtle.right(90)
    __peano(turtle, n-1, d/3)


def __dragon(turtle, n, d):
    if not n:
        turtle.forward(d)
        return
    turtle.left(45)
    __dragon(turtle, n-1, d/sqrt(2))
    turtle.right(90)
    __dragon_reverse(turtle, n-1, d/sqrt(2))
    turtle.left(45)


def __dragon_reverse(turtle, n, d):

    if not n:
        turtle.forward(d)
        return
    turtle.right(45)
    __dragon(turtle, n-1, d/sqrt(2))
    turtle.left(90)
    __dragon_reverse(turtle, n-1, d/sqrt(2))
    turtle.right(45)


def __btree(turtle, n, d):
    if not n:
        turtle.forward(d)
        turtle.back(d)
        return
    color = (255, 0, 0) if n < 3 else (188, 143, 53)
    turtle.color(color)
    turtle.forward(d)
    turtle.left(45)
    __btree(turtle, n-1, d/2)
    turtle.right(90)
    __btree(turtle, n-1, d/2)
    turtle.left(45)
    turtle.back(d)


def __ptree_base(turtle, n, d):
    for _ in range(4):
        turtle.forward(d)
        turtle.right(90)
    if not n:
        return

    turtle.forward(d)
    turtle.left(degrees(atan(0.75)))
    __ptree_base(turtle, n-1, 4*d/5)
    turtle.right(90)
    turtle.forward(4*d/5)
    __ptree_base(turtle, n-1, 3*d/5)
    turtle.back(d*4/5)
    turtle.left(degrees(atan(4/3)))
    turtle.back(d)


def __ptree_mod(turtle, n, d, alpha):
    for _ in range(4):
        turtle.forward(d)
        turtle.right(90)
    if not n:
        return
    turtle.forward(d)
    turtle.left(alpha)
    __ptree_mod(turtle, n-1, d*cos(radians(alpha)), alpha)
    turtle.right(90)
    turtle.forward(d*cos(radians(alpha)))
    __ptree_mod(turtle, n-1, d*sin(radians(alpha)), alpha)
    turtle.back(d*cos(radians(alpha)))
    turtle.left(90-alpha)
    turtle.back(d)


def __leaf(turtle, d):
    for _ in range(3):
        turtle.forward(d)
        turtle.right(90)
    turtle.penup()
    turtle.forward(d)
    turtle.pendown()
    turtle.right(90)


def __branch(turtle, d):
    for _ in range(2):
        turtle.forward(d)
        turtle.right(90)
        turtle.penup()
        turtle.forward(d)
        turtle.pendown()
        turtle.right(90)


def __ptree_notrunk(turtle, n, d, alpha):
    if n >= 3:
        turtle.color(198, 141, 24)
    else:
        turtle.color(0, int(100+155/(n+1)), 0)
    if not n:
        __leaf(turtle, d)
        return
    __branch(turtle, d)
    turtle.forward(d)
    turtle.left(alpha)
    __ptree_notrunk(turtle, n-1, d*cos(radians(alpha)), alpha)
    turtle.right(90)
    turtle.penup()
    turtle.forward(d*cos(radians(alpha)))
    turtle.pendown()
    __ptree_notrunk(turtle, n-1, d*sin(radians(alpha)), alpha)
    turtle.penup()
    turtle.back(d*cos(radians(alpha)))
    turtle.pendown()
    turtle.left(90-alpha)
    turtle.penup()
    turtle.back(d)
    turtle.pendown()


def __ptree_tilt(turtle, n, d):
    if n >= 3:
        turtle.color(198, 141, 24)
    else:
        turtle.color(0, int(100+155/(n+1)), 0)
    import random
    if not n:
        __leaf(turtle, d)
        return

    __branch(turtle, d)
    alpha = 15 + random.randint(0, 60)
    turtle.forward(d)
    turtle.left(alpha)
    __ptree_tilt(turtle, n-1, d*cos(radians(alpha)))
    turtle.right(90)
    turtle.penup()
    turtle.forward(d*cos(radians(alpha)))
    turtle.pendown()
    __ptree_tilt(turtle, n-1, d*sin(radians(alpha)))
    turtle.penup()
    turtle.back(d*cos(radians(alpha)))
    turtle.pendown()
    turtle.left(90-alpha)
    turtle.penup()
    turtle.back(d)
    turtle.pendown()
