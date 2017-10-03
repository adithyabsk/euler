#!/usr/bin/env python

# ALGORITHM: Sieve of Eratosthenes
# Strong algorithm for numbers less than 10 000 000

# http://stackoverflow.com/questions/19345627/python-prime-numbers-sieve-of-eratosthenes

def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = range(np1)
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
    return filter(None, s)

print sum(sieve(2000000))

