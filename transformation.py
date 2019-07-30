import zipfile
import boto3
import io
import urllib.request
import pg8000

##Read in zip file from s3
myurl = "https://s3-us-west-2.amazonaws.com/com.guild.us-west-2.public-data/project-data/the-movies-dataset.zip"
# with urllib.request.urlopen(myurl) as url:
#     zip_file = url.read()
file_name, headers = urllib.request.urlretrieve(myurl)


print(file_name)
##Unzip zip file
with file_name.ZipFile(zip_file, mode='r') as zipf:
    for subfile in zipf.namelist():
        print(subfile)



def parse_movie():
	##Code to ingest and transform cast data
	print("Code to ingest and transform cast data")

def ingest_cast():
	##Code to ingest and transform cast data
	print("Code to ingest and transform cast data")

def ingest_crew():
	##Code to ingest and transform crew data
	print("Code to ingest and transform crew data")

def write_data(table_name, data):
	##Code to ingest and transform crew data
	print("Code to ingest and transform crew data")


if __name__ == '__main__':
    movie_data = parse_movie()
    cast_data = parse_cast()
    crew_data = parse_crew()