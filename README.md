# Connect PostgreSQL database with Python

In this section, I'll explain how to connect your PostgreSQL database to Python and query it.

## Install "Psycopg2"

To access the PostgreSQL database, Python needs a PostgreSQL driver. You must first install the `Psycopg2` package on your computer.

```bash
python -m pip install psycopg2
```

## Import Psycopg2"

To access the PostgreSQL database, import `psycopg2` library into your Python code.

```python
import psycopg2
```

## Creating a Database:

For the purpose of example, we will need a sample database. To do so, follow the below steps:

- First, open a PostgreSQL client tool like `pgadmin4` or `psql`.
- Second login to the database using your credentials.
- Finally, run the following command to create a database (for example, `company`).

```sql
CREATE DATABASE company;
```

## Create Connection:

To connect to the above created database (i.e., `company`), we use the `connect()` function. 
So, establish a connection to the database. Use your PostgreSQL database's username and password in the Python code.

```python
mydb = psycopg2.connect(
  host="localhost",
  user="yourUsername",
  password="yourPassword",
  database="company"
)
```

## Make Cursor:

You must create or include a `cursor()` in your Python code in order to run SQL queries.

```python
mycursor = mydb.cursor()
```

Now you can use SQL commands to query the database.

## Commit Changes:

You also have to include the commit function and set automatic commit to be `true`.

```python
mydb.set_session(autocommit=True)
```

So that each action is committed or saved without having to call `mydb.commit()` after each command.

## Query the Database:

Now create a table in the database using the cursor we created.

```python
mycursor.execute('''CREATE TABLE employee(
    EmployeeID int,
    Name varchar(255),
    Email varchar(255));
''')
```

## Insert Data Into Table:

Now we are inserting the values into the database.

```python
mycursor.execute('''
INSERT INTO employee (EmployeeID, Name, Email)
    VALUES (101, 'Mark', 'mark@company.com'),
           (102, 'Robert', 'robert@company.com'),
           (103, 'Spencer', 'spencer@company.com');
''')
```

## Retrive the Data:

Now let’s query the database.

```python
mycursor.execute("SELECT * FROM employee")
```

It’s important to note that after the query executes, you still need to use one of the `psycopg2` functions to retrieve data rows.

- fetchone()
- fetchall()
- fetchmany()

For example,

```python
print(mycursor.fetchone())
```

| EmployeeID | Name | Email            |
| :--------- | :--- | :--------------- |
| 101        | Mark | mark@company.com |

The most basic way to fetch data from your database is to use the `fetchone()` function. This function will return exactly one row (the first row) after executing the SQL query.

```python
print(mycursor.fetchall())
```

| EmployeeID | Name    | Email               |
| :--------- | :------ | :------------------ |
| 101        | Mark    | mark@company.com    |
| 102        | Robert  | robert@company.com  |
| 103        | Spencer | spencer@company.com |

If you need more than one row from your database, you can use `fetchall()`, which works the same as `fetchone()` except that it returns all the rows.

```python
print(mycursor.fetchmany(2))
```

| EmployeeID | Name   | Email              |
| :--------- | :----- | :----------------- |
| 101        | Mark   | mark@company.com   |
| 102        | Robert | robert@company.com |

With `fetchmany()`, you have another option to retrieve multiple records from the database and have more control over the exact number of rows retrieved.

You can use any of them depending on your needs.

## Close the Connection:

In the end, you must close the cursor and the connection.

```python
mycursor.close()
mydb.close()
```

You can also get code snippet from [here](https://github.com/kishlayjeet/Connect-PostgreSQL-database-to-Python/blob/d7c5cae0a809ec0714cf193c5db6a77f30e70502/code-snippet.py).

## Authors

I am [Kishlay](https://www.github.com/kishlayjeet), and I have written this tutorial, but other people have also helped me with it.
If you have any trouble with this tutorial, please tell me about it, and I will make it better.
If you like this tutorial and this helped you out, then please give it a star.

## Feedback

If you have any feedback, please reach out to me at contact.kishlayjeet@gmail.com
