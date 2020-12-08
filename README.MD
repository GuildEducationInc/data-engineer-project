# Overview
The goal of this project is to get an idea of:
* Your ability to work with and grok data 
* Your software engineering skill 
* Your data pipeline design skill 


The data used for this project will be The Movies Dataset (pulled from https://www.kaggle.com/rounakbanik/the-movies-dataset).
Please use the copy of the data set provided at https://s3-us-west-2.amazonaws.com/com.guild.us-west-2.public-data/project-data/the-movies-dataset.zip
 
# Deliverables
There are three goals to this project:
* Design a data model that can be used to answer a series of questions. 
* Implement a program that transforms the input data into a form usable by the data model
* Explain how you would scale this pipeline

The designed data model must be able to at least answer the following questions: 

* Production Company Details:
    * budget per year
    * revenue per year
    * profit per year
    * releases by genre per year
    * average popularity of produced movies per year
    
* Movie Genre Details:
    * most popular genre by year
    * budget by genre by year
    * revenue by genre by year
    * profit by genre by year


## Code 
Clone this repo and provide the final tarball of the finished product. The code should be written in Java or Python
* Code must be runnable - Document how to build/run the code
* Code must solve the problem at hand (this is not supposed to be a big data problem)
* Code must contain SQL query for gathering `Movie Genre Details:revenue by genre by year` with your data model
* Input: should take a s3 endpoint to the file as a positional argument (e.g. `cmd s3://com.guild.us-west-2.public-data/project-data/the-movies-dataset.zip`)
* Output: 
  * Directory that contains the output files of the processed data
  * Error log file

## Data Model
Please provide a data model that meets the following requirements:
* Document describing modeling decisions
* Relational ERD diagram (included relationships) 
* Evolvable for future needs (don’t just aggregate the exact questions) 

## Design
The goal of the design task is to see how you would scale and maintain the system.
* Propose solutions for an 100x increase in data volume, and an hourly update cadence
* Propose ideas for data reprocessing:
  * How would you go about backfilling 1 year worth of data?
  * How would you avoid impact on the production flow (e.g. concurrent job runs)?
* What kind of error handling would you put in place?

Be sure to discuss issues and trade-offs around scaling, monitoring, failure recovery, authentication, etc... 
