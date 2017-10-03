#!/usr/bin/env python

N = 1001

for x in range(1, N):
	y = x+1
	z = y+1
	while z <= N:
		while z**2 < x**2 + y**2:
			z+=1
		if  z**2 == x**2 + y**2 and z <= N:
			if x + y + z == 1000:
				print x, y, z
		y+=1

# This program runs in quadratic time:
# http://stackoverflow.com/questions/575117/generating-unique-ordered-pythagorean-triplets
# It is much better than looping through every
# single iterative value lower than 1000
