"""Sabermetrics Part 2 --- Baseball game simulator

References
----------

* http://www.seanlahman.com/files/database/readme2017.txt
using mookie betts 2017 season to start

"""

import random

def getbattingaverage(hits, atbats):
	return (round(hits / atbats, 3))

def getonbasepercentage(hits, walks, hbp, atbats):
	return (round(((hits + walks + hbp) / atbats), 3))

def choose_length():
	number_at_bats = int(input("Enter length for simulator: "))
	return number_at_bats

def ballinplay(number_at_bats):
	loop = 0
	while loop <= number_at_bats:
		rnum = round(random.random(), 3)
		batting = getbattingaverage(166, 628)
		balls = 0
		strikes = 0
		outs = 0
		hits = 0
		strike_out = 0

		while strikes < 3:
			print (rnum)
			if batting >= rnum:
				print ("There is a ball in play!")
				strikes = 4
				hits += 1
			else:
				print ("There is no ball in play.")
				rnum = round(random.random(), 3)
				strikes += 1

		if strikes == 3:
			print("The player has struck out.")
			outs += 1
			loop += 1
			strike_out += 1
		else:
			print("The player is on base.")
			loop += 1

		if outs == 3:
			print("The inning has ended.")
	print('Number of Hits: ' + str(hits))
	print('Number of Strike Outs: ' + str(strike_out))

def main():
	ballinplay(choose_length())

if __name__ == '__main__':
	main()

