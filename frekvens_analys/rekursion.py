"""This program multiplies two numbers x,y by adding the
first number x to itself y times.

Author: Simon Johansson
Estimated time: An hour
Actual Time: Half an hour"""

def multiply(number1, number2):
    result = 0
    if number2 != 0:
        if number2 < 0:
            result += multiply(number1, number2 + 1)
            result -= number1
        elif number2 > 0:
            result += multiply(number1, number2 - 1)
            result += number1
        return result
    else:
        return result

print(multiply(3,5))