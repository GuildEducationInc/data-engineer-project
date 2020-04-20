
import unittest
from unittest.mock import patch

class TestMainFunctions(unittest.TestCase):


    def test_extract_dim_genres(self):
        pass

    def test_extract_production_company(self):
        pass

    def test_extract_dim_movies(self):
        pass

    def test_extract_fact_movies(self):
        pass

    @patch('MySQL.pymysql.connect')
    def test_connection(self, mock_connect):
        pass

if __name__ == '__main__':
    unittest.main()
