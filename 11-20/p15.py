#!/usr/bin/env python

from math import *

# How many paths can you take from the top left of a grid to
# the bottom right of a grid?

# The answer is mathematically a combination of steps to the
# right and steps down. There must be an equal number of both
# Hence, the answer must revolve around the combinatorial
# solution of 2n chose n. 

N = 20

print factorial(2*N)/((factorial(N))**2)