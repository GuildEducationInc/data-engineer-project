import zipfile
import boto3
import io
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
from utilities import get_db,do_query


##Read in zip file from s3
myurl = "https://s3-us-west-2.amazonaws.com/com.guild.us-west-2.public-data/project-data/the-movies-dataset.zip"
# with urllib.request.urlopen(myurl) as url:
#     zip_file = url.read()
file_object =  urllib2.urlopen(myurl)

zip_file = file_object.read()
##Unzip zip file
with file_name.ZipFile(zip_file, mode='r') as zipf:
    for subfile in zipf.namelist():
        print(subfile)



def parse_movie():
	##Code to ingest and transform cast data
	print("Code to ingest and transform cast data")

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
    	do_query(connection,movie_insert_query)

