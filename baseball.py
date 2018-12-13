from sqlalchemy import create_engine
import argparse
import pandas as pd
import sqlite3
import csv

def main():
	argparsesqlite()

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

if __name__ == '__main__':
	main()