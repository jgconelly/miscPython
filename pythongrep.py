import re
import argparse
import multiprocessing as mp
import glob

def main(): 
	argparsegrp()

def argparsegrp():
	parser = argparse.ArgumentParser()
	parser.add_argument("grep", help="Nothing but grep")
	parser.add_argument("grep_file_path" , help='File path to grep')
	args = parser.parse_args()
	full_grep = grep_process(args.grep, args.grep_file_path)

def grep_process(grep_term, grep_file_path):
	def process(line):
		if grep_term in line:
			print (line)
	with open(grep_file_path) as f:
		for line in f:
			process(line)
	re_grep(grep_term, grep_file_path)		

def re_grep(grep_term, grep_file_path):
	p = re.compile('grep_term')
	m = p.search(grep_file_path)
	result = re.search(grep_term, grep_file_path)
	print (type(result))

if __name__ == '__main__':
	p = mp.Process(target=main)
	p.start()
	p.join()