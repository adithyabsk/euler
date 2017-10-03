#!/usr/bin/env python

# Find the sum of the digits in the number 100!

def factorial(n): return n*factorial(n-1) if n >=1 else 1

print sum(map(int, str(factorial(100))))