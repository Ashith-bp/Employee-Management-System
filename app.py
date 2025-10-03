import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="ems_db"
    )

def add_employee(name, dept, salary):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)", (name, dept, salary))
    db.commit()
    db.close()
    print("Employee added successfully.")

def view_employees():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(row)
    db.close()

def update_employee(emp_id, salary):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE employees SET salary=%s WHERE id=%s", (salary, emp_id))
    db.commit()
    db.close()
    print("Employee updated successfully.")

def delete_employee(emp_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    db.commit()
    db.close()
    print("Employee deleted successfully.")

def main():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee Salary")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            dept = input("Enter department: ")
            salary = float(input("Enter salary: "))
            add_employee(name, dept, salary)
        elif choice == "2":
            view_employees()
        elif choice == "3":
            emp_id = int(input("Enter employee ID: "))
            salary = float(input("Enter new salary: "))
            update_employee(emp_id, salary)
        elif choice == "4":
            emp_id = int(input("Enter employee ID: "))
            delete_employee(emp_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
