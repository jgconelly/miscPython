"""Sabermetrics Part 2 --- Baseball game simu

References
----------

* http://www.seanlahman.com/files/database/readme2017.txt
using mookie betts 2017 season to start

"""

import pandas as pd
import random

def main():
	ba = getBattingAverage(166, 628)
	obp = getOnbasePercentage(166, 77, 2, 628)
	print (ba, obp)
	ballInPlay()

def getbattingaverage(hits, atbats):
	return (round(hits / atbats, 3))

def getonbasepercentage(hits, walks, hbp, atbats):
	return (round(((hits + walks + hbp) / atbats), 3))

#def getpitchingstats(per_strikes, per_balls, ipouts):
#	percentage_strikes = 


def ballinplay():
	batting = getBattingAverage(166, 628)
	rnum = round(random.random(), 3)
	balls = 0
	strikes = 0
	outs = 0

	while strikes < 3:
		print (rnum)
		if batting >= rnum:
			print ("There is a ball in play!")
			strikes = 4
		else:
			print ("There is no ball in play.")
			rnum = round(random.random(), 3)
			strikes += 1

	if strikes == 3:
		print("The player has struck out.")
		outs += 1
	else:
		print("The player is on base.")

	if outs == 3:
		print("The inning has ended.")


if __name__ == '__main__':
	main()

