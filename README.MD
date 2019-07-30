# Bryan Linton Notes

Data Model is stored as data_model.pdf

Here are some things I thought were worth mentioning:
* Used dbdiagram.io to generate the data model
* Dimension tables start with d_, fact tables start with f_ in the star schema model
* Normalized the model as much as possible
* Included created at, updated at, and last action id (user or service principal that made the last update to that column) columns to track and audit history
* Broke out things like language into it's own dimension in case the movie adds a language in the future (e.g. Toy Story creates a German Version in 2021)
* Started using branching policy only after getting in core files (don't actually need to do this if it's only me but thought it would be worth doing anyway)
* Only created one ingestion function, and one api function (i.e. endpoint) due to time constraints, but you can see how the rest would be implemented in the same fashion

If I were actually building this out for a team and had more time I would implement the following:
* More thorough data model
* Implement data model in a PostreSQL DB with DDL and some sort of DB Version control (such as flyway: https://flywaydb.org/)
* Create a dev guide to help with onboarding new developers to this project in the README.md
* More Object Oriented Python design with classes rather than just a single Python file that does everything
* API would be configured where each function in my api.py script would be it's own lambda function triggered by AWS API Gateway, routed to an appropriate DNS (e.g. www.guild.com/api/v1/movies)
* More thorough unit tests to verify that the transformations were being done properly
* More API endpoints 

This took me a total of x minutes to complete.  There's a lot more I'd like to implement here, but obviously understand you guys want to see what can be done given an alotted time.



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
When designing the system focus on the high level design of the system and how parts of it will interact. 
You don't need to go very deep on the API, don't worry about defining routes/types/etc. 

Assumptions: 
* New data files are received monthly
* The system should be scalable

The design should include: 
* Data transformation - using the program implemented above
* Data storage - How will the data be stored?
* Data serving - How will users access the data?

Be sure to discuss issues and trade-offs around scaling, monitoring, failure recovery, authentication, etc... 


# Bryan Linton Notes

Data Model is stored as data_model.pdf

Here are some things I thought were worth mentioning:
* Used dbdiagram.io to generate the data model
* Dimension tables start with d_, fact tables start with f_ in the star schema model
* Normalized the model as much as possible
* Included created at, updated at, and last action id (user or service principal that made the last update to that column) columns to track and audit history
* Broke out things like language into it's own dimension in case the movie adds a language in the future (e.g. Toy Story creates a German Version in 2021)
* Started using branching policy only after getting in core files (don't actually need to do this if it's only me but thought it would be worth doing anyway)

If I were actually building this out for a team and had more time I would implement the following:
* More thorough data model
* More Object Oriented Python design with classes rather than just a single Python file that does everything
* API would be configured where each function in my api.py script would be it's own lambda function triggered by AWS API Gateway, routed to an appropriate DNS (e.g. www.guild.com/api/v1/movies)
* More thorough unit tests to verify that the transformations were being done properly
* More API endpoints 

This took me a total of x minutes to complete.  There's a lot more I'd like to implement here, but obviously understand you guys want to see what can be done given an alotted time.  Let me know if you'd like to see more and I can hop back on and add more to this Repository.