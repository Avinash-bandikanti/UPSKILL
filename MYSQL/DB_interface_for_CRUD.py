import mysql.connector
import sys
connection=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Abhi@131'
)
cursor=connection.cursor()
def create():
    cursor.execute('create database if not exists employee_database')
    cursor.execute("use employee_database")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            Id INT PRIMARY KEY,
            Name VARCHAR(255) NOT NULL,
            Date_of_joining DATE,
            Salary DECIMAL(10,2),
            Title VARCHAR(255),
            Location VARCHAR(255)
         )
    """)
    connection.commit()
    print("Database created successfully")
def insert_employee(id,name, date_of_joining,salary,title,location):
    cursor.execute("use employee_database")
    insert_query = "INSERT INTO employees (id,name,date_of_joining,salary,title,location) VALUES (%s,%s, %s, %s, %s,%s)"
    employee_data = (id,name,date_of_joining,salary,title,location)
    cursor.execute(insert_query, employee_data)
    connection.commit()
    print("Employee details upload successfully.")
def read(id):
    cursor.execute("use employee_database")
    read_query = "SELECT * FROM employees WHERE id=%s"
    identity = id
    cursor.execute(read_query, (identity,))
    result = cursor.fetchone()
    if result:
        print("Employee details")
        print(f"Employee id:", result[0])
        print(f"Employee name:", result[1])
        print(f"Employee doj:",result[2])
        print(f"Employee salary:", result[3])
        print(f"Employee title:", result[4])
        print(f"Employee location:", result[5])
    else:
        print("Employee not found")
def is_employee_id_present(employee_id):
    cursor.execute('use employee_database')
    select_query = "SELECT id FROM employees WHERE id = %s"
    cursor.execute(select_query, (employee_id,))
    result = cursor.fetchone()
    if result:
        new_name = input("Enter a name:")
        new_doj = input("Enter doj:")
        new_sal = float(input("Enter sal:"))
        new_title = input("Enter a title:")
        new_location = input("Enter a location:")
        update_employee(new_emp_id, new_name, new_doj, new_sal, new_title, new_location)
    else:
        print("Employee id is not found")

def update_employee(id,name,date_of_joining,salary,title,location):
    cursor.execute("use employee_database")
    update_query="UPDATE employees SET name = %s,date_of_joining=%s,salary=%s,title=%s,location=%s WHERE id=%s"
    update_data=(name,date_of_joining,salary,title,location,id)
    cursor.execute(update_query,update_data)
    connection.commit()
    print("updation successfully")

def delete(id):
    cursor.execute('use employee_database')
    select_query = "SELECT id FROM employees WHERE id = %s"
    identity = id
    cursor.execute(select_query, (identity,))
    result = cursor.fetchone()
    if result:
        cursor.execute("use employee_database")
        delete_query="DELETE from employees WHERE id =%s"
        cursor.execute(delete_query,(identity,))
        print("Delete successfully")
    else:
        print("Employee id not found")
    connection.commit()

def e():
    sys.exit()
while(1):
    print("1.CREATE\t2.INSERT\t3.READ\t4.UPDATE\t5.DELETE\t6.EXIT")
    choice=int(input("Enter your choice:"))
    if choice==1:
        create()
    if choice==2:
        employee_id=int(input("Enter id:"))
        employee_name = input("Enter employee name: ")
        employee_doj=input("Enter doj:")
        employee_salary = float(input("Enter employee salary: "))
        employee_title = input("Enter employee title: ")
        employee_location = input("Enter employee location: ")
        insert_employee(employee_id,employee_name, employee_doj, employee_salary,employee_title,employee_location)

    if choice==3:
        new_id = int(input("Enter id:"))
        read(new_id)
    if choice==4:
        new_emp_id = int(input("Enter a id:"))
        is_employee_id_present(new_emp_id)
    if choice==5:
        del_id = int(input("Enter id:"))
        delete(del_id)
    if choice==6:
        connection.close()
        e()


