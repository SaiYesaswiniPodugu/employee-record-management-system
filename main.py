import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yesaswini@2004",
    database="employee_management"
)

cursor = conn.cursor()

while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        designation = input("Enter Designation: ")
        salary = float(input("Enter Salary: "))

        query = """
        INSERT INTO employees
        (first_name,last_name,designation,salary)
        VALUES (%s,%s,%s,%s)
        """

        values = (
            first_name,
            last_name,
            designation,
            salary
        )

        cursor.execute(query, values)
        conn.commit()

        print("Employee Added Successfully!")

    elif choice == "2":

        cursor.execute("SELECT * FROM employees")

        records = cursor.fetchall()

        print("\nEmployee Records\n")

        for row in records:
            print(row)

    elif choice == "3":

        emp_id = int(input("Enter Employee ID: "))

        query = """
        SELECT *
        FROM employees
        WHERE employee_id=%s
        """

        cursor.execute(query, (emp_id,))

        employee = cursor.fetchone()

        if employee:
            print("\nEmployee Found:")
            print(employee)
        else:
            print("Employee Not Found")

    elif choice == "4":

        emp_id = int(input("Enter Employee ID: "))
        new_salary = float(input("Enter New Salary: "))

        query = """
        UPDATE employees
        SET salary=%s
        WHERE employee_id=%s
        """

        cursor.execute(query, (new_salary, emp_id))
        conn.commit()

        print("Salary Updated Successfully!")

    elif choice == "5":

        emp_id = int(input("Enter Employee ID to Delete: "))

        query = """
        DELETE FROM employees
        WHERE employee_id=%s
        """

        cursor.execute(query, (emp_id,))
        conn.commit()

        print("Employee Deleted Successfully!")

    elif choice == "6":

        print("Program Closed")
        break

    else:

        print("Invalid Choice")

cursor.close()
conn.close()