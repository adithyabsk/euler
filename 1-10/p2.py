#!/usr/bin/env python

fibo_sum = 0
s1 = 0
s2 = 1
while s2 < 4000000:
	temp = s2
	s2 = s1+s2
	s1 = temp
	if s2 % 2 == 0:
		fibo_sum+=s2
print fibo_sum
