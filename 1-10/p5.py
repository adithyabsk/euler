#!/usr/bin/env python
import math
from collections import Counter

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

factorLists = range(2, 21)
instances = {}
for i in range(2, 21):
	instances[i] = 0
for i in range(0, len(factorLists)):
	factorLists[i] = prime_factors(factorLists[i])
for factorList in factorLists:
	inst = Counter(factorList)
	for key, value in inst.iteritems():
		if instances[key] < value: instances[key] = value
val = 1
for key, value in instances.iteritems():
	print key, value
	if value:
		val*=key**value
print val