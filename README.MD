# Overview
The goal of this project is to get an idea of:
* Your ability to work with and grok data 
* Your software engineering skill 
* Your system design skill 


The data used for this project will be The Movies Dataset (pulled from https://www.kaggle.com/rounakbanik/the-movies-dataset).
Please use the copy of the data set provided at https://s3-us-west-2.amazonaws.com/com.guild.us-west-2.public-data/project-data/the-movies-dataset.zip
# Requirements

There are three goals to this project:
* Design a data model that can be used to answer a series of questions. 
* Implement a program that transforms the input data into a form usable by the data model
* Design a system that can leverage the data model and program to provide real time access to the data (This is a design task, do not implement)

The designed data model must expose the following information: 

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

# Deliverables

Fork this repository and complete all relevant tasks in that forked repository

## Data Model 
Please provide a visual diagram of the chosen data model. 


## Implementation
The input for the program will be the raw data (CSV files) in The Movies Dataset.
The output for the program will be one or more files that can be used to hydrate the data model. 

Feel free to use any language you are comfortable with. (A JVM language or Python is preferable if possible)


## Design
The goal of the design task is to design a system that exposes this data to end users via an HTTP API.

Assumptions: 
* New data files are received monthly
* The system should be scalable

The design should include: 
* Data transformation - using the program implemented above
* Data storage - How will the data be stored?
* Data serving - How will users access the data?

Be sure to discuss issues and trade-offs around scaling, monitoring, failure recovery, authentication, etc... 
