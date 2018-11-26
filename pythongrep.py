import re
import argparse
import multiprocessing as mp
#import glob

def main(): 
	argparsegrp()

def argparsegrp():
	parser = argparse.ArgumentParser()
	parser.add_argument("grep", help="Nothing but grep")
	parser.add_argument("grep_file_path" , help='File path to grep')
	args = parser.parse_args()
	full_grep = re_grep(args.grep, args.grep_file_path)	

def re_grep(grep_term, grep_file_path): #Using Regular expressions
		for line in open(grep_file_path).readlines():
			if re.search(grep_term, line):
				print (line.rstrip())

if __name__ == '__main__':
	p = mp.Process(target=main)
	p.start()
	p.join()

