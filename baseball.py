"""Sabermetrics Part 1 --- CSV File loader

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
	parser.add_argument("file_path", help="Location of CSV file to load")
	parser.add_argument("name_of_table" , help='Name of the new table to create in the sqlite3 db. ')
	parser.add_argument("database", help='Name of the database to load data')
	args = parser.parse_args()
	importing(args.database, args.file_path, args.name_of_table)

def importintosqlite(csvfile, name): #Old function
	engine = create_engine('sqlite://', echo=False)
	imported_df = pd.read_csv(csvfile)
	imported_df.to_sql(str(name), con=engine)
	engine.execute("select * from Parks limit 5").fetchall()

#"/Users/Azreal/Downloads/baseballdatabank-master/core/Parks.csv"

def importing(database, file_path, name_of_table): #new function
    conn = create_connection(database) #create a database connection
    with conn as conn:
    	if conn is not None:
    		imported_df = pd.read_csv(file_path)
    		imported_df.to_sql(name_of_table, con=conn, index=False, if_exists='replace')
    	else:
        	print("Error, cannot create the database connection.")

def create_connection(db_file): #Function to create connection to sqlite3 db
	try: 
		conn = sqlite3.connect(db_file)
		return conn
	except error as e:
		print (e)

	return None

def create_table(conn, create_table_sql): #Function to create table in sqlite3 db
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except error as e:
		print(e)		

if __name__ == '__main__':
	main()