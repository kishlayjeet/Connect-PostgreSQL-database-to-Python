import psycopg2

mydb = psycopg2.connect(
  host="localhost",
  user="yourUsername",
  password="yourPassword",
  database="company"
)

mycursor = mydb.cursor()

mydb.set_session(autocommit=True)

mycursor.execute('''CREATE TABLE employee(  
      EmployeeID int,  
      Name varchar(255),  
      Email varchar(255));
''')

mycursor.execute('''
  INSERT INTO employee (EmployeeID, Name, Email) 
      VALUES (101, 'Mark', 'mark@company.com'),
             (102, 'Robert', 'robert@company.com'),
             (103, 'Spencer', 'spencer@company.com');
''')

mycursor.execute("SELECT * FROM employee")

print(mycursor.fetchall())

mycursor.close()
mydb.close()