from sqlalchemy import create_engine
import pandas as pd
import sqlite3
import csv

#engine = create_engine('sqlite:///baseball.sqlite')

def importintosqlite(csvfile):
	imported_df = pd.read_csv(csvfile)
	imported_df.to_sql(table_name, if_exists='append', index=False)
