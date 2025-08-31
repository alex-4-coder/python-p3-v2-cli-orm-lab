# lib/helpers.py
from models.employee import Employee
from models.department import Department

# -------------------------------
# Employee Helpers (Options 7–13)
# -------------------------------

def list_employees():
    employees = Employee.all()
    for emp in employees:
        print(emp)

def find_employee_by_name():
    name = input("Enter the employee's name: ").strip()
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")

def find_employee_by_id():
    try:
        emp_id = int(input("Enter the employee's id: ").strip())
    except ValueError:
        print("Invalid ID")
        return
    employee = Employee.find_by_id(emp_id)
    if employee:
        print(employee)
    else:
        print(f"Employee {emp_id} not found")

def create_employee():
    try:
        name = input("Enter the employee's name: ").strip()
        job_title = input("Enter the employee's job title: ").strip()
        dept_id = int(input("Enter the employee's department id: ").strip())

        # Check department exists
        department = Department.find_by_id(dept_id)
        if not department:
            print("Error creating employee:  department_id must reference a department in the database")
            return

        employee = Employee(name=name, job_title=job_title, department_id=dept_id)
        employee.save()
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error creating employee:  {e}")

def update_employee():
    try:
        emp_id = int(input("Enter the employee's id: ").strip())
    except ValueError:
        print("Invalid ID")
        return

    employee = Employee.find_by_id(emp_id)
    if not employee:
        print(f"Employee {emp_id} not found")
        return

    try:
        name = input("Enter the employee's new name: ").strip()
        if name:
            employee.name = name
        else:
            raise ValueError("name must be a non-empty string")

        job_title = input("Enter the employee's new job title: ").strip()
        if job_title:
            employee.job_title = job_title
        else:
            raise ValueError("job_title must be a non-empty string")

        dept_id = int(input("Enter the employee's new department id: ").strip())
        department = Department.find_by_id(dept_id)
        if department:
            employee.department_id = dept_id
        else:
            raise ValueError("department_id must reference a department in the database")

        employee.save()
        print(f"Success: {employee}")
    except Exception as e:
        print(f"Error updating employee:  {e}")

def delete_employee():
    try:
        emp_id = int(input("Enter the employee's id: ").strip())
    except ValueError:
        print("Invalid ID")
        return

    employee = Employee.find_by_id(emp_id)
    if employee:
        employee.delete()
        print(f"Employee {emp_id} deleted")
    else:
        print(f"Employee {emp_id} not found")

def list_department_employees():
    try:
        dept_id = int(input("Enter the department's id: ").strip())
    except ValueError:
        print("Invalid ID")
        return

    department = Department.find_by_id(dept_id)
    if not department:
        print(f"Department {dept_id} not found")
        return

    for emp in department.employees():
        print(emp)

