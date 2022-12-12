import os
import unittest
from unittest import mock, TestCase

import sqlalchemy
import pandas as pd

environs = {
    "synthea_user": "test",
    "synthea_password": "test",
    "synthea_host": "localhost",
    "synthea_port": "5432",
    "synthea_database": "synthea"
}


@mock.patch.dict(os.environ, environs)
class MainTestCase(TestCase):
    def test_get_credentials(self):
        from main import get_credentials
        credentials = get_credentials()
        assert isinstance(credentials, dict)
        assert all(key in credentials for key in ["username", "password", "host", "port", "database"])

    def test_get_engine(self):
        # Test the get_engine function
        from main import get_engine
        engine = get_engine()
        assert isinstance(engine, sqlalchemy.engine.Engine)

    @mock.patch('main.pd.read_sql_query')
    def test_get_query(self, read_sql_query_mock):
        # Test the get_query function
        from main import get_query
        read_sql_query_mock.return_value = pd.DataFrame()
        df = get_query("SELECT * FROM native.patients LIMIT 1")
        assert isinstance(df, pd.DataFrame)

    @mock.patch('main.pd.read_sql_query')
    def test_get_person(self, read_sql_query_mock):
        # Test the get_person function
        from main import get_person
        read_sql_query_mock.return_value = pd.DataFrame()
        df = get_person(["b1b636dd-9283-7f8d-0985-6de0a614d22a", "3395432e-acd1-9141-adcc-41a5f9222d7d"])
        assert isinstance(df, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()
