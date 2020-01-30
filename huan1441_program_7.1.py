# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Name: ABE65100 Lab02 Exercise 7.1
#
# Purpose: Script that tests the square root algorithm (Newton's method),
#          and compares it with math.sqrt.
#
# Author: Tao Huang (huan1441)
#
# Created: Jan 24, 2020
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import math

def test_square_root(a,x):
    """Function to compute the square root of a with Newton's method and math.sqrt.
    x is an arbitrary initial value.
    """
    epsilon = 1e-16
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            column_1 = float(a)
            column_2 = "{column_2:<13}".format(column_2=float(round(x,11)))
            column_3 = "{column_3:<13}".format(column_3=float(round(math.sqrt(a),11)))
            column_4 = round(abs(x-math.sqrt(a)),27)
            print(column_1,column_2,column_3,column_4)
            break
        x = y

for a in range(1,10):
    test_square_root(a,1)
