"""Sabermetrics Part 1 --- CSV File loader

Part 1 of 3 in the sabermetrics project. This script loads csv files into a sqlite3 database. 
Sqlite was chosen because of its simplicity and locks are currently not an issue. 
This script functions by reading in csv files one at a time which can be done through the command line
given the argparser function. 

References
----------

* http://www.seanlahman.com/files/database/readme2017.txt

"""

import argparse
import pandas as pd
import sqlite3
import csv

def main():
    argparsesqlite()

def argparsesqlite():
	parser = argparse.ArgumentParser()
	parser.add_argument('file_path', help='File path of CSV file to load.')
	parser.add_argument('name_of_table' , help='Name of the new table to create in the sqlite3 db. ')
	parser.add_argument('database', help='Name of the database to load data into.')
	args = parser.parse_args()
	importing(args.database, args.file_path, args.name_of_table)

def importing(database, file_path, name_of_table): 
	"importing function to bring data into sqlite3 table"
    conn = create_connection(database)
    with conn as conn:
    	if conn is not None:
    		imported_df = pd.read_csv(file_path)
    		imported_df.to_sql(name_of_table, con=conn, index=False, if_exists='replace')
    	else:
        	print("Error, cannot create the database connection.")

def create_connection(db_file):
	"function to create connection to sqlite3 database"
	try: 
		conn = sqlite3.connect(db_file)
		return conn
	except error as e:
		print (e)

	return None

def create_table(conn, create_table_sql):
	"function to create table in sqlite3 database"
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except error as e:
		print(e)		

if __name__ == '__main__':
	main()
