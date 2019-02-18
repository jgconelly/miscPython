"""Sabermetrics Part 2 --- Baseball game simulator

References
----------
* http://www.seanlahman.com/files/database/readme2017.txt
using mookie betts 2017 season to start
"""

import random

def getbattingaverage(hits, atbats):
	"Batting average calculation"
	return (round(hits / atbats, 3))

def getonbasepercentage(hits, walks, hbp, atbats):
	"Onbase percentage calculation"
	return (round(((hits + walks + hbp) / atbats), 3))

def choose_length():
	"Currently this is the number of at bats to simulate for a given player."
	number_at_bats = int(input("Enter length for simulator: "))
	return number_at_bats

def reset_rand_num():
	rnum = round(random.random(), 3)
	return rnum

def ballinplay(number_at_bats):
	"Using random number generator to simulate a player batting"
	loop = 1
	balls = 0
	strikes = 0
	outs = 0
	hits = 0
	strike_out = 0

	batting = getbattingaverage(166, 628)
	rnum = round(random.random(), 3)

	while loop <= number_at_bats:
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
			strikes = 0
			rnum = round(random.random(), 3)
		else:
			print("The player is on base.")
			loop += 1
			strikes = 0
			rnum = round(random.random(), 3)

		if outs == 3:
			print("The inning has ended.")
	print('Number of Hits: ' + str(hits))
	print('Number of Strike Outs: ' + str(strike_out))
	print('Batting Average: ' + str(hits/number_at_bats))

def main():
	number_at_bats = choose_length()
	ballinplay(number_at_bats)

if __name__ == '__main__':
	main()

