# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Name: ABE65100 Lab02 Exercise 5.2
#
# Purpose: Script for checking whether the given lengths of three sticks could
#          be arranged in a triangle.
#
# Author: Tao Huang (huan1441)
#
# Created: Jan 24, 2020
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def is_triangle(x,y,z):
    """A function that checks whether the given lengths of three sticks could
       be arranged in a triangle. x, y and z is the lenth of three sticks,repectively.
    """
    if x+y<z or x+z<y or y+z<x:
        print("No")
    else:
        print("Yes")

# a function that determine whether a number is positive

def is_positive(n):
    try:
        int(n)
    except:
        return False
    else:
        if int(n) <= 0:
            return False
        else:
            return True

# a function that uses three input lengths to check whether they can form a triangle

def sticks_triangle():    

    while True:
        x = int(float(input("Please enter the lenth of the first stick: ")))
        if is_positive(x):
            break
        else:
            print("This is not a positive number. Please enter again!")
            
    while True:
        y = int(float(input("Please enter the lenth of the second stick: ")))
        if is_positive(y):
            break
        else:
            print("This is not a positive number. Please enter again!")

    while True:
        z = int(float(input("Please enter the lenth of the third stick: ")))
        if is_positive(z):
            break
        else:
            print("This is not a positive number. Please enter again!")

    is_triangle(x,y,z)

sticks_triangle()       
            
