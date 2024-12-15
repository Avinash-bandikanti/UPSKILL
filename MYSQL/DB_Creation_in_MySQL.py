import mysql.connector
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Abhi@131'
)
cursor=connection.cursor()
create_database_query='create database if not exists employee_database'
cursor.execute(create_database_query)
connection.commit()
cursor.close()
connection.close()
print("Database created successfully")
