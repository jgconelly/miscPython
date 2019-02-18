"""
Daily Coding Problem 1: 
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

from itertools import combinations

test_list = [10, 15, 3, 7]

def test_for_k(total):
	"Using itertools combinations to create pairs to sum"
	for i in combinations(test, 2):
		if sum(i) == total:
			print("yes")
		else:
			print("No")
	
test_for_k(17)