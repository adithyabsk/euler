#!/usr/bin/env python

# Convert words to letters and then count the letters

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

converter = {
	"1": "one",
	"2": "two",
	"3": "three",
	"4": "four",
	"5": "five",
	"6": "six",
	"7": "seven",
	"8": "eight",
	"9": "nine",
	"10": "ten",
	"11": "eleven",
	"12": "twelve",
	"13": "thirteen",
	"14": "fourteen",
	"15": "fifteen",
	"16": "sixteen",
	"17": "seventeen",
	"18": "eighteen",
	"19": "nineteen",
	"20": "twenty",
	"30": "thirty",
	"40": "forty",
	"50": "fifty",
	"60": "sixty",
	"70": "seventy",
	"80": "eighty",
	"90": "ninety",
	"100": "hundred",
	"1000": "thousand"
}

def num_to_word(i):
	num_str = str(i)
	rslt = ""
	if len(num_str) == 4: return "one"+converter[num_str]
	if len(num_str) >= 1:
		if i % 10 != 0:
			rslt = converter[num_str[-1]]
	if len(num_str) >= 2:
		tens = num_str[-2:]
		tens_place = num_str[-2]
		if int(tens_place) != 0:
			if (int(tens) < 20) or (int(tens) % 10 == 0): rslt = converter[tens]
			else: rslt = converter[num_str[-2]+"0"]+rslt
	if len(num_str) >= 3:
		hundreds = num_str[-3:]
		hundreds_place = num_str[-3]
		if rslt: rslt =  converter[hundreds_place]+converter["100"]+"and"+rslt
		else: rslt =  converter[hundreds_place]+converter["100"]
	return rslt

x = [len(num_to_word(i)) for i in range(1, 1001)]
print sum(x)


