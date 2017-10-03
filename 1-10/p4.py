#!/usr/bin/env python
palindromes = []
for i in range(100, 1000):
	for j in range(100, 1000):
		n = str(i*j)
		if len(n)%2:
			continue
		if n[:len(n)/2] == n[len(n)/2:][::-1]:
			palindromes.append(int(n))
print max(palindromes)						