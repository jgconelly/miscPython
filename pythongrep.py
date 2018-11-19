import re
#from multiprocessing import Process, freeze_support, set_start_method

def main(): #please note, this is for python 2.x. Will need to be updated to python 3.x when moved to github
	grep_term = input("Please Enter Search Term:")
	grep_file_path = input("Please Enter File Path:")

	def process(line):
		if grep_term in line:
			print (line)

	with open(grep_file_path) as f:
		for line in f:
			process(line)

	result = re.match(grep_term, grep_file_path)

#python_grep()

"""
if __name__ == '__main__':
    set_start_method('spawn')
    p = Process(target=main)
    p.start()
"""
if __name__ == '__main__':
    main()