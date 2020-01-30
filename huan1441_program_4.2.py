# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Name: ABE65100 Lab02 Exercise 4.2
#
# Purpose: Script for drawing flowers as in Figure 4.1
#
# Author: Tao Huang (huan1441)
#
# Created: Jan 24, 2020
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import turtle
import math

bob = turtle.Turtle()

# speed the turtle to the fastest
bob.speed(0)
bob.screen.delay(0)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them. t is a turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and
    angle (in degrees). t is a turtle.
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def flowers(t,r,pt,angle):
    """Draws a flower with n petals.
    t: turtle
    r: radius of the arcs
    pt: number of petals
    angle: angle (degrees) of the arcs
    """
    flw_angle_1 = 180 - angle
    flw_angle_2 = 360 / pt
    
    for i in range(pt):
        for j in range(2):
            arc(t,r,angle)
            t.lt(flw_angle_1)
        t.lt(flw_angle_2)

# draw the 7-petal flower in the Figure 4.1

flowers(bob,100,7,60)

bob.pu()
bob.fd(200)
bob.pd()

# draw the 10-petal flower in the Figure 4.1

flowers(bob,80,10,80)

bob.pu()
bob.fd(200)
bob.pd()

# draw the 20-petal flower in the Figure 4.1

flowers(bob,250,20,20)

turtle.mainloop()
