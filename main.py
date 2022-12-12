import os
import pandas as pd

from sqlalchemy import create_engine, text
from sqlalchemy.engine.url import URL


def get_credentials():
    """
    Reads the credentials from the user system and returns a dictionary
    with the necessary information to connect to the database.

    Returns
    -------
    dict
        A dictionary containing the credentials to connect to the database
    """
    # Read the credentials from the user system
    username = os.environ.get("synthea_user", None) or input("Enter your username: ")
    password = os.environ.get("synthea_password", None) or input("Enter your password: ")
    host = os.environ.get("synthea_host", None) or input("Enter the hostname: ")
    port = os.environ.get("synthea_port", None) or input("Enter the port: ")
    database = os.environ.get("synthea_database", None) or input("Enter the database name: ")

    # Return the credentials as a dictionary
    return {
        "username": username,
        "password": password,
        "host": host,
        "port": port,
        "database": database,
    }


def get_engine():
    """
    Returns a SQLAlchemy engine to connect to the database.

    Returns
    -------
    sqlalchemy.engine.Engine
        A SQLAlchemy engine to connect to the database
    """
    # Get the credentials to connect to the database
    credentials = get_credentials()

    # Create a SQLAlchemy engine using the given credentials
    engine = create_engine(URL.create(drivername="postgresql", **credentials))

    return engine


# Get a SQLAlchemy engine to connect to the database
engine = get_engine()


def get_query(query):
    """
    Executes the given SQL query and returns the result as a pandas DataFrame.

    Parameters
    ----------
    query : str or sqlalchemy.TextClause
        The SQL query to be executed

    Returns
    -------
    pandas.DataFrame
        The result of the SQL query as a pandas DataFrame
    """
    # Execute the given SQL query and store the result in a pandas DataFrame
    df = pd.read_sql_query(query, engine)

    return df


def get_person(patient_ids):
    """
    Queries the person table with the given patient ids and returns the result
    as a pandas DataFrame.

    Parameters
    ----------
    patient_ids : list
        A list of patient ids

    Returns
    -------
    pandas.DataFrame
        The result of the SQL query as a pandas DataFrame
    """
    # Create the SQL query to be executed
    query = text(
        """ 
        SELECT *
        FROM native.patients
        WHERE id IN :values; 
    """)
    query = query.bindparams(values=tuple(patient_ids))

    # Execute the SQL query and return the result as a pandas DataFrame
    return get_query(query)


if __name__ == '__main__':
    print(get_person(["b1b636dd-9283-7f8d-0985-6de0a614d22a", "3395432e-acd1-9141-adcc-41a5f9222d7d"]))
