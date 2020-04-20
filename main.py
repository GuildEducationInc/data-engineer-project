import logging
import pandas as pd
import os
from process import Database

db = Database()


def extract_dim_genres():
    """
    This function checks if the source csv file exist.
    If so, it ran some simple transformation logics and
    then it calls the insert_into_table function to insert
    to the dim_genres table
    """
    pass


def extract_dim_production_company():
    """
    This function checks if the source csv file exist.
    If so, it ran some simple transformation logics and
    then it calls the insert_into_table function to insert
    to the dim_production_company table
    """
    pass


def extract_dim_movies():
    """
    This function checks if the source csv file exist.
    If so, it ran some simple transformation logics and
    then it calls the insert_into_table function to insert
    to the dim_movies table
    """
    pass


def extract_fact_movies():
    """
    This function checks if the source csv file exist.
    If so, it ran some simple transformation logics and
    then it calls the insert_into_table function to insert
    to the fact_movies table
    """
    # get project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    # look for the movie_metadata csv file
    movies_path = os.path.join(project_dir, 'data/movies_metadata.csv')
    if os.path.exists(movies_path):
        df_movies_raw = pd.read_csv(movies_path)
        columns_to_map = [
        'id', 'original_title', 'belongs_to_collection', 'original_language',
        'production_companies', 'production_countries', 'release_date',
        'genres', 'budget', 'popularity', 'revenue', 'runtime',
        'production_companies', 'overview'
        ]
        df_movies = df_movies_raw[columns_to_map]
        df_movies = df_movies.rename(columns={"id": "movie_id",
                                "original_title": "movie_name"})
        for _, row in df_movies.iterrows():
            db.insert_into_table('fact_movies', row)

def main():
    """
    This is the main entry point of the data process of movies data sets
    It tries extract data and then insert into different fact 
    and dimentional tables
    """
    try:
        extract_fact_movies()
        logging.info('Extract fact movies done')
        extract_dim_genres()
        logging.info('Extract dim generes done')
        extract_dim_production_company()
        logging.info('Extract production company done')
    except OSError:
        logging.info('Can not process files')
    except Exception as e:
        raise e


if __name__=="__main__":
    main()