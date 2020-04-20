import logging
import os
import json
import pymysql
import boto3
from botocore.exceptions import ClientError

class Database:
    def __init__(self):
        self.rds_host = os.environ['RDS_HOST']
        self.rds_name = os.environ['RDS_USERNAME']
        self.db_name = os.environ['RDS_DB_NAME']
        self.password = None
        self.conn = None

    def get_secret(self):
        """
        Store the RDS db password in aws secret manager
        with a KMS key encrypted so it is more secure
        """
        session = boto3.session.Session()
        secret_name = os.environ['SECRET_NAME'] 
        client = session.client(
            service_name='secretsmanager',
            region_name='us-east-1'  #as an example
        )
        try:
            self.password = client.get_secret_value(
                SecretId=secret_name
            )
            #logic not complete
            # More to add. KMS key decryption etc
        except ClientError as e:
            raise e

    def db_connection(self):
        """Connect to MySQL Database."""
        try:
            if (conn is None):
                conn = pymysql.connect(
                    self.rds_host, user=self.rds_name, passwd=self.password,
                     db=self.db_name, connect_timeout=5)
            elif (not conn.open):
                conn = pymysql.connect(
                    self.rds_host, user=self.rds_name, passwd=self.password,
                     db=self.db_name, connect_timeout=5)
        except pymysql.MySQLError as e:
            logging.error(e)
            raise e
        finally:
            logging.info('Connection opened successfully.')


    def insert_into_table(self, table_name, data):
        """
        Generate dynamic query to run the insert functions
        table_name: string pass in the table_name manually
        data: data frame
        """
        project_dir = os.path.dirname(os.path.abspath(__file__))
        schema_path = os.path.join(project_dir, 'table_schema.json')
        # read table schema
        with open(schema_path) as schema_file:
            table_schema = json.load(schema_file)
        # generate dynamic insert query
        query = (f"INSERT INTO {table_name} {table_schema[table_name]}"
                f"VALUES {data}; ")
        try:
            self.db_connection()
            with self.conn.cursor() as cur:
                cur.execute(query)
                cur.close()
                logging.info(f'{table_name} get updated successfully.')
        except pymysql.MySQLError as e:
            logging.error(e)
        finally:
            if conn:
                conn.close()
                conn = None
                logging.info('Database connection closed.')
