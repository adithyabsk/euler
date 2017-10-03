#!/usr/bin/env python

def collatz(terms):
	prev = terms[-1:][0]
	if prev == 1:
		return terms
	else:
		if prev%2 == 0:
			term = prev/2
			terms.append(term)
			return collatz(terms)
		else:
			term = 3*prev+1
			terms.append(term)
			return collatz(terms)

collatz_lengths = []
for i in range(1, 1000000):
	collatz_lengths.append(len(collatz([i])))

print collatz_lengths.index(max(collatz_lengths))+1