#!/usr/bin/env python

primes  = [2]
attempt = 3
while len(primes) < 10001:
	if all(attempt % prime != 0 for prime in primes):
		primes.append(attempt)
	attempt += 2
print primes[-1]