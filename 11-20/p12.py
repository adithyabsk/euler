#!/usr/bin/env python

total = 0
count = 0

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

while(True):
	count+=1
	total+=count
	facs = factors(total)
	if len(facs) > 500:
		break

print total

