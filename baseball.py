from sqlalchemy import create_engine
import argparse
import pandas as pd
import sqlite3
import csv

def main():
    database = "/Users/Azreal/Documents/miscPython/test.db"
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
    	imported_df = pd.read_csv("/Users/Azreal/Downloads/baseballdatabank-master/core/Parks.csv")
    	imported_df.to_sql("parks", con=conn, index=False, if_exists='replace')
    else:
        print("Error! cannot create the database connection.")

def importintosqlite(csvfile, name):
	engine = create_engine('sqlite://', echo=False)
	imported_df = pd.read_csv(csvfile)
	imported_df.to_sql(str(name), con=engine)
	engine.execute("select * from Parks limit 5").fetchall()

def argparsesqlite():
	parser = argparse.ArgumentParser()
	parser.add_argument("csvfile", help="Location of CSV file to load")
	parser.add_argument("name" , help='Name of the new table to create in the sqlite3 db. ')
	args = parser.parse_args()
	full_grep = importintosqlite(args.csvfile, args.name)

def create_connection(db_file):
	try: 
		conn = sqlite3.connect(db_file)
		return conn
	except error as e:
		print (e)

	return None

def create_table(conn, create_table_sql):
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
	except error as e:
		print(e)		

if __name__ == '__main__':
	main()