# Connect PostgreSQL Database with Python

This tutorial explains how to connect your PostgreSQL database to Python and query it.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python: You can download and install Python from the official website (https://www.python.org).
- PostgreSQL: Install PostgreSQL on your computer by following the instructions from the official website (https://www.postgresql.org).

## Install the "psycopg2" Package

To access the PostgreSQL database, Python needs a PostgreSQL driver. You can install the `psycopg2` package using pip, the Python package installer. Open your command prompt or terminal and run the following command:

```bash
pip install psycopg2
```

## Import the "psycopg2" Library

To use the `psycopg2` package in your Python code, import the `psycopg2` module:

```python
import psycopg2
```

## Creating a Database

For the purpose of this example, we will need a sample database. Follow the steps below to create it:

1. Open a PostgreSQL client tool like `pgadmin4` or `psql`.
2. Log in to the database using your credentials.
3. Run the following command to create a database, for example, `company`:

```sql
CREATE DATABASE company;
```

## Create Connection

To connect to the previously created database (`company`), we use the `connect()` function. Establish a connection to the database by providing your PostgreSQL database's username, password, and database name in the Python code:

```python
mydb = psycopg2.connect(
  host="localhost",
  user="yourUsername",
  password="yourPassword",
  database="company"
)
```

## Create a Cursor

You need to create a cursor to execute SQL queries in your Python code:

```python
mycursor = mydb.cursor()
```

Now you can use SQL commands to query the database.

## Commit Changes

You also need to include the commit function and set the automatic commit to be `True`:

```python
mydb.set_session(autocommit=True)
```

This ensures that each action is committed or saved without having to call `mydb.commit()` after each command.

## Query the Database

Now, let's create a table in the database using the cursor we created:

```python
mycursor.execute('''CREATE TABLE employee(
    EmployeeID int,
    Name varchar(255),
    Email varchar(255));
''')
```

## Insert Data Into Table

Now, let's insert values into the database:

```python
mycursor.execute('''
INSERT INTO employee (EmployeeID, Name, Email)
    VALUES (101, 'Mark', 'mark@company.com'),
           (102, 'Robert', 'robert@company.com'),
           (103, 'Spencer', 'spencer@company.com');
''')
```

## Retrieve the Data

Let's query the database:

```python
mycursor.execute("SELECT * FROM employee")
```

After executing the query, you can use one of the `psycopg2` functions to retrieve data rows:

- `fetchone()`: Retrieves exactly one row (the first row) after executing the SQL query.
- `fetchall()`: Retrieves all the rows.
- `fetchmany()`: Retrieves a specific number of rows.

For example:

```python
print(mycursor.fetchone())
```

Output:

| EmployeeID | Name | Email            |
| :--------- | :--- | :--------------- |
| 101        | Mark | mark@company.com |

The most basic way to fetch data from your database is to use the `fetchone()` function. It returns exactly one row (the first row) after executing the SQL query.

```python


print(mycursor.fetchall())
```

Output:

| EmployeeID | Name    | Email               |
| :--------- | :------ | :------------------ |
| 101        | Mark    | mark@company.com    |
| 102        | Robert  | robert@company.com  |
| 103        | Spencer | spencer@company.com |

If you need more than one row from your database, you can use `fetchall()`, which returns all the rows.

```python
print(mycursor.fetchmany(2))
```

Output:

| EmployeeID | Name   | Email              |
| :--------- | :----- | :----------------- |
| 101        | Mark   | mark@company.com   |
| 102        | Robert | robert@company.com |

With `fetchmany()`, you have another option to retrieve a specific number of rows from the database.

Choose the appropriate function based on your needs.

## Close the Connection

Finally, remember to close the cursor and the connection:

```python
mycursor.close()
mydb.close()
```

You can also find the code snippet [here](https://github.com/kishlayjeet/Connect-PostgreSQL-database-to-Python/blob/d7c5cae0a809ec0714cf193c5db6a77f30e70502/code-snippet.py).

## Authors

This tutorial was written by [Kishlay 
Jeet](https://www.github.com/kishlayjeet), with contributions from other people.
If you encounter any issues with this tutorial, please let me know, and I will make improvements.
If you found this tutorial helpful, please consider giving it a star.

## Feedback

If you have any feedback, please reach out to me at contact.kishlayjeet@gmail.com.
