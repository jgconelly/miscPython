from sqlalchemy import create_engine
import argparse
import pandas as pd
import sqlite3
import csv

def main():
    database = "/Users/Azreal/Documents/miscPython/test.db"
 
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
 
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        # create tasks table
        create_table(conn, sql_create_tasks_table)
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