"""Sabermetrics Part 2 --- Baseball game simulator

References
----------
* http://www.seanlahman.com/files/database/readme2017.txt
using mookie betts 2017 season to start
"""

import argparse
import logging

from bisect import bisect
from itertools import cycle
from random import random, seed

OPTIONS = 'Single', 'Double', 'Triple', 'Homerun', 'Out'

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

def argparsebb():
    #number_at_bats = choose_length()
    #ballinplay(number_at_bats)
    "Main entry point for testing as a script."
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--iterations', type=int, default=1000000)
    parser.add_argument('-s', '--seed', type=int, default=None)
    parser.add_argument('-v', '--verbose', action='store_const',
                        const=logging.DEBUG, default=logging.INFO)
    args = parser.parse_args()
    seed(args.seed)
    logging.basicConfig(level=args.verbose, format='%(message)s')
    wins = test(args.iterations)
    logging.info('Win ratio: %.3f', wins / args.iterations)

def test(iterations):
    "Simulate multiple games and return number of wins."
    lineups = (
        cycle([  # away team
            (90, 120, 130, 135, 535),   # .252 BA
            # ^-- 90 Singles, 30 Doubles, 10 Triples, 5 Homeruns, 400 Outs
            (80, 100, 105, 125, 525),   # .238 BA
            (70, 100, 110, 160, 555),   # .288 BA
            ()
        ]),
        cycle([  # home team
            (100, 130, 140, 150, 500),  # .300 BA
            # ^-- 100 Singles, 30 Doubles, 10 Triples, 10 Homeruns, 350 Outs
            (100, 130, 140, 150, 500),  # .300 BA
            (100, 130, 140, 150, 500),  # .300 BA
        ]),
    )
    wins = sum(simulate_game(lineups) for _ in range(iterations))
    return wins

def simulate_game(lineups):
    "Simulate one game of baseball and return win/loss."
    # pylint: disable=too-many-locals
    inning = 1
    scores = [0, 0]
    away, home = 0, 1  # indexes for scores

    def advance(count):
        "Advance the runners on base by count."
        nonlocal first, second, third
        for _ in range(count):
            scores[team] += third
            first, second, third = 0, first, second

    logging.debug('Starting Game')

    while inning <= 9 or scores[away] == scores[home]:
        logging.debug('Inning %s', inning)
        for team in (away, home):
            logging.debug('%s Team at Bat', 'Home' if team else 'Away')
            outs = 0
            first = 0
            second = 0
            third = 0
            while outs < 3:
                weights = next(lineups[team])
                total = weights[-1]
                limit = len(weights) - 1
                offset = random() * total
                choice = bisect(weights, offset, 0, limit)
                option = OPTIONS[choice]
                if option == 'Single':
                    advance(1)
                    first = 1
                elif option == 'Double':
                    advance(2)
                    second = 1
                elif option == 'Triple':
                    advance(3)
                    third = 1
                elif option == 'Homerun':
                    advance(3)
                    scores[team] += 1
                else:
                    option == 'Out'
                    outs += 1
                log = '%9s Outs: %s/3 Bases: [%s, %s, %s] Score: %s-%s'
                logging.debug(log, option, outs, first, second, third, *scores)
        inning += 1

    return scores[home] > scores[away]


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
    argparsebb()

if __name__ == '__main__':
    main()

