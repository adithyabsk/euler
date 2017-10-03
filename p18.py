#!/usr/bin/env python

# Find the maximum of the triangle
# E.g.
#
#     3
#    7 4
#   2 4 6
#  8 5 9 3
# 
# 3 + 7 + 4 + 9 = 23

# Do the same for the triangle below

# This was hard, you did it wrong multiple times, initially you used a greedy algorithm.
# That shit is WRONG... because that finds a local maximum wheras you are looking for a global
# maximum. This distinction and thus lends to a bottom up approach

# See this stackoverflow post for why you were damn wrong:
# https://stackoverflow.com/questions/8002252/euler-project-18-approach

triangle = [[75],
			[95, 64],
			[17, 47, 82],
			[18, 35, 87, 10],
			[20,  4, 82, 47, 65],
			[19,  1, 23, 75,  3, 34],
			[88,  2, 77, 73,  7, 63, 67],
			[99, 65,  4, 28, 06, 16, 70, 92],
			[41, 41, 26, 56, 83, 40, 80, 70, 33],
			[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
			[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
			[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
			[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
			[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
			[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]


def triangle_calc(t):
	if len(t) > 1:
		row_add = []
		next_to_last_row = t[-2]
		last_row = t[-1]
		for i in range(len(last_row)):
			if i != len(last_row) - 1:
				row_add.append(max(last_row[i:i+2]))
		t[-2] = [a+b for a,b in zip(next_to_last_row, row_add)]
		return triangle_calc(t[:-1])
	else:
		return t[0][0]

print triangle_calc(triangle)


