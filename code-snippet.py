import psycopg2 

# Creation of the connection class

class Connection:
  def __init__(self):
    try:
      self.connection = psycopg2.connect(
        host = "localhost",
        user = "yourUsername",
        password = "yourPassword",
        database = "company"
      )
      self.cursor = self.connection.cursor()
    except Exception as e:
      print(f"Error: {e}")

    self.cursor.execute("""CREATE TABLE Employee(
      EmployeeID int,
      name varchar(255),
      email varchar(255)
    );
    """)

  # Creation of the method that inserts data

  def insertData(self, name, email):
    cursor = self.cursor
    sql = "INSERT INTO Employee (name, email) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (name, email))
        self.connection.commit()
        print("Data inserted successfully")
    except Exception as e:
        self.connection.rollback()
        print(f"Error inserting data: {e}")

  # An instance of the connection class is created

  connection = Connection()
  
  # Insert data into table 

  connection.insertData("Mark", "mark@company.com")
  connection.insertData("Robert", "robert@company.com")
  connection.insertData("Spencer", "spencer@company.com")
