import re
import argparse
import multiprocessing as mp

def main(): 
	argparsegrp()
	#process_input()
	grep_term = "split"
	grep_file_path = "/Users/Azreal/Documents/jcrosalind/dictionaries5.py"
	def process(line):
		if grep_term in line:
			print (line)
	with open(grep_file_path) as f:
		for line in f:
			process(line)
	result = re.match(grep_term, grep_file_path)

def argparsegrp():
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", help="A count of selected lines is written to a standard ouput")
	args = parser.parse_args()
	if args.c:
		print (args.echo)

#def process_input():
#	grep_term = input("Please Enter Search Term:")
#	grep_file_path = input("Please Enter File Path:")
#	return grep_term, grep_file_path

#def grep_process(grep_term, grep_file_path):
#	if grep_term in line:
#		print(line)
#	with open(grep_file_path) as f:
#		for line in f:
#			process(line)
#	result = re.match(grep_term, grep_file_path)


if __name__ == '__main__':
	p = mp.Process(target=main)
	p.start()
	p.join()
    #main()