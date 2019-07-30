import zipfile
import boto3
import io
import urllib2


##Read in zip file from s3
myurl = "https://s3-us-west-2.amazonaws.com/com.guild.us-west-2.public-data/project-data/the-movies-dataset.zip"
with urllib2.urlopen(myurl) as url:
    zip_file = url.open()


##Unzip zip file
with zipfile.ZipFile(zip_file, mode='r') as zipf:
    for subfile in zipf.namelist():
        print(subfile)


