# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
# Name: ABE65100 Lab02 Exercise 6.5
#
# Purpose: Script that prompts the user for two values,
#          and then computes the greatest common divisor (GCD).
#
# Author: Tao Huang (huan1441)
#
# Created: Jan 24, 2020
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# A function to compute the GCD of two numbers

def gcd():
    x = int(float(input("Please enter the first number: ")))
    y = int(float(input("Please enter the second number: ")))

    # make that x is always greater than y
    
    if x >= y:
        x, y = (x, y)
    else:
        x, y = (y, x)

    try:
        remainder = x % y

        # if remainder is zero, gcd(x,y) = y
        # if remainder is not zero, gcd(x,y) = gcd(y,remainder)
    
        while remainder != 0:
            x = y
            y = remainder
            remainder = x % y
        print("The greatest common divisor is",y)

    # if y is zero, gcd(x,0) = x
    
    except ZeroDivisionError:
        print("The greatest common divisor is",x)
    
gcd()
