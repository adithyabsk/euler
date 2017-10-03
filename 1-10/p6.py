#!/usr/bin/env python

def squareOfSums(i, f):
	sos = 0
	for i in range(i, f+1):
		sos += i
	return sos**2

def sumOfSquares(i, f):
	sos = 0
	for i in range(i, f+1):
		sos += i**2
	return sos

initial = 1
final   = 100

print squareOfSums(initial, final) - sumOfSquares(initial, final)