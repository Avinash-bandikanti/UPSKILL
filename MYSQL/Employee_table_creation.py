import mysql.connector
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Abhi@131'
)
cursor=connection.cursor()
cursor.execute('create database if not exists employee_database')
cursor.execute('use employee_database')
cursor.execute("""
      create table if not exists employees(
      Id int primary key,
      Name varchar(255) not null,
      Date_of_joining date,
      Salary decimal(10,2),
      Title varchar(255),
      Location varchar(255)
      )
""")
connection.commit()
cursor.close()
connection.close()
print("Employees table created successfully")
