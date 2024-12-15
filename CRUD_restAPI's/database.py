import mysql.connector
import json

def load_config():
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)
    return config_data

def get_database_connection():
    config = load_config()
    return mysql.connector.connect(**config['DATABASE_CONFIG'])

def get_employees():
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Employees')
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return employees

def add_employee(Employee_id,Employee_Name, Employee_DateOfJoining,Employee_salary,Employee_title,Employee_location):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Employees (Id,Name,Date_of_joining,Salary,Title,Location) VALUES (%s,%s,%s, %s,%s,%s)', (Employee_id,Employee_Name, Employee_DateOfJoining,Employee_salary,Employee_title,Employee_location))
    connection.commit()
    cursor.close()
    connection.close()

def get_employee(Employee_id):
    connection = get_database_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM Employees WHERE Id=%s', (Employee_id,))
    employee = cursor.fetchone()
    cursor.close()
    connection.close()
    return employee
def update_employee(Employee_id,Employee_Name, Employee_DateOfJoining,Employee_salary,Employee_title,Employee_location):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE Employees SET  Name=%s, Date_of_joining=%s,Salary=%s,Title=%s,Location=%s WHERE Id=%s', (Employee_Name, Employee_DateOfJoining,Employee_salary,Employee_title,Employee_location,Employee_id))
    connection.commit()
    cursor.close()
    connection.close()
def delete_employee(Employee_id):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Employees WHERE Id=%s', (Employee_id,))
    connection.commit()
    cursor.close()
    connection.close()
