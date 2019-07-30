import zipfile
import boto3
import io
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from utilities import get_db,do_query
import csv
import pandas

def parse_movie():
	movies_table = []

	##Read in movie file
	with open('movie_file.csv') as movie_csv:
	    content = csv.reader(movie_csv)
	    headers = next(content, None)
	    #Append relevant columns to movies table
	    for row in content:
	        title = row[8]
	        release_date = row[14]
	        runtime = row[16]
	        movies_table.append([title,release_date,runtime])
	return movies_table

def parse_cast():
	##Code to ingest and transform cast data
	print("Code to ingest and transform cast data")

def parse_crew():
	##Code to ingest and transform crew data
	print("Code to ingest and transform crew data")


if __name__ == '__main__':
	#connection = get_db()
    movie_data = parse_movie()
    cast_data = parse_cast()
    crew_data = parse_crew()
    #Would do the below for all tables
    for row in movie_data:
    	title = row[0]
    	release_date = row[1]
    	runtime = row[2]
    	#can do this for the rest of the rows
    	movie_insert_query = "INSERT INTO d_movie (title,release_date,runtime,created_at,updated_at,last_action_id) VALUES ('{0}','{1}',{2},now(),now(),1);".format(title,release_date,runtime)
    	try:
            #do_query(connection,movie_insert_query)
            print("Inserted {} into d_movies".format(row))
    	except:
            print("Error Inserting movie {}.  Movie already exists in DB or there was a connection issue".format(title))

