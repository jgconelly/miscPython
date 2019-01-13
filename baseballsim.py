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

def getBattingAverage(hits, atbats):
	return (round(hits / atbats, 3))

def getOnbasePercentage(hits, walks, hbp, atbats):
	return (round(((hits + walks + hbp) / atbats), 3))

def ballInPlay():
	batting = getBattingAverage(166, 628)
	rnum = round(random.random(), 3)
	balls = 0
	strikes = 0
	outs = 0

	while strikes < 3:
		print (rnum)
		if batting >= rnum:
			print ("There is a ball in play!")
		else:
			print ("There is no ball in play.")
			strikes += 1

	if strikes == 3:
		print("The player has struck out.")
		outs += 1
		
	if outs == 3:
		print("The inning has ended.")


if __name__ == '__main__':
	main()

