[![Build and Test](https://github.com/wanghewen/synthea_query/actions/workflows/build-and-test.yml/badge.svg)](https://github.com/wanghewen/synthea_query/actions/workflows/build-and-test.yml)

# Requirement:

1. PostgreSQL are installed somewhere.

# Task 1

1. Put the SQL files into the code folder.

2. Import the generated synthetic data into the database:

```bash
psql -U your_super_user_name -f dump-synthea-202212120538.sql
```

This SQL is exported from the PostgreSQL database.
The data inside is generated using Synthea 2.7.0 and imported using the ETL tool provided in the reference.
The data is generated using the following command (no need to run this):

```bash
java -jar .\synthea-with-dependencies.jar -s 12 -p 100 --exporter.csv.export true
```

3. Create 2 users: user1 and readonly:

```bash
psql -U your_super_user_name -d synthea -f create_user.sql
```

4. Create a query using table joins and where clause:

```bash
psql -U your_super_user_name -d synthea -f create_query.sql
```

Inside the SQL files there are explanations and optimizations of the query.

# Task 2

1. Install relevant dependencies

```bash
pip install -r requirements.txt
```

2. Setup environment variables for PostgreSQL, for example:

```bash
export synthea_user=test synthea_password=test synthea_host=localhost synthea_port=5432 synthea_database=synthea
```

3. Run main.py and get test results

```bash
python main.py
```

4. To run unit tests:

```bash
python -m unittest tests.test_main
```

# Task 3

The github repository is here: [https://github.com/wanghewen/synthea_query](https://github.com/wanghewen/synthea_query)