#!/usr/bin/env python

K = 600851475143
factors = []
for i in range(2,  int(K**(0.5))):
	while K%i == 0:
		K = K/i
		factors.append(i)
print factors
print max(factors)
