""" Example Python Program for Pascal's Triangle Assignment

This example simply generates a Fibonnaci sequence and graphs the result.

"""

import matplotlib.pyplot as pyplot
import math


def fib_series(length):
    """ Creates the Fibonnaci sequence.

    This function takes in the length of the desired series and returns
    the sequence (as a list).

    For your solution, please include a similar function that takes
    in the depth of the triangle and returns a list of lists (2d list)
    such that each level is represented by a list:

    [ [1],
      [1, 1],
      [1, 2, 1],
      [1, 3, 3, 1] ]
    
    """

    # Seed the start of the series
    y = [0,1]

    # calculate the next item in the Fib. sequence
    for i in range(length - 2):
        y.append(y[i]+y[i+1])

    return y


y = fib_series(14)
# For your solution, please plot the level (x) vs. the sum of the row.
# Remember, every row/level of Pascal's triangle will sum to 2**i
# where that is 2 raised to the level number, starting with 0.
pyplot.plot(range(len(y)),y)
pyplot.show()
