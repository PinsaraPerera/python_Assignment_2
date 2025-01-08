import os

class Employee:
    def __init__(self, id, name, salary, department):
        self.id = id,
        self.name = name,
        self.salary = salary,
        self.department = department

    def increase_salary(self, percentage):
        _new_total_percentage = (100 + percentage)/100
        self.salary *= _new_total_percentage

    def update_department(self, department):
        self.department = department

    def display_details(self):
        print(f'Employee ID: {self.id}')
        print(f'Employee Name: {self.name}')
        print(f'Employee Salary: {self.salary}')
        print(f'Employee Department: {self.department}')

class FileNotFoundException(Exception):
    pass

class EmployeeNotFoundException(Exception):
    pass

class EmployeeDatabase:
    def __init__(self):

        self.employees = []

    def load_file(self):
        if os.path.exists('Employee_Management_System/data.txt'):
            with open('Employee_Management_System/data.txt', 'r') as file:
                data = file.read()
                records = data.split('\n')

            for record in records:
                employee_detail = record.split(',')
                employee_detail = [_val.strip() for _val in employee_detail]
                _id, _name, _salary, _department = employee_detail

                self.employees.append({"id": _id, "name": _name, "salary": _salary, "department": _department})
        else:
            raise FileNotFoundException("File is not found")

    def add_employee(self, employee: Employee):

        if employee:
            self.employees.append({"id": employee.id, "name": employee.name, "salary": employee.salary, "department": employee.department})
        else:
            raise EmployeeNotFoundException("Employee data not confirmed")

    def remove_employee(self, employee: Employee):
        
        self.employees = [_employee for _employee in self.employees if _employee["id"] != employee.id]

    def update_employee(self, employee: Employee):

        for _employee in self.employees:
            if _employee["id"] == employee.id:
                _employee["name"] = employee.name
                _employee["salary"] = employee.salary
                _employee["department"] = employee.department

                break

    def dislay_all(self):
        for index, _employee in self.employees:
            print(f'\t{index}) {_employee['id'], _employee['name'], _employee['salary'], _employee['department']}\n')

    def save_to_file(self):
        content = ''
        with open('Employee_Management_System/data.txt', 'w') as file:
            for _employee in self.employees:
                content += f'{_employee['id'], _employee['name'], _employee['salary'], _employee['department']}\n'


if __name__ == "__main__":
    
    while True:
        print("~~~~~~~~~~~ MENU ~~~~~~~~~~~~~~~")
        print("a) Add new Employees.")
        print("b) Remove employee.")
        print("c) Update employee detail(salary, department).")
        print("d) Display all employees.")
        print("e) Save and load records from a file.")

        _input = input("Choose an option: ")

        database = EmployeeDatabase()

        if _input == 'a':
            id = input("Enter the ID: ")
            name = input("Enter the Name: ")
            salary = float(input("Enter the Salary: "))
            department = input("Enter the Department: ")

            employee = Employee(id, name, salary, department)
            database.add_employee(employee=employee)

            print("Employee Added Successfully")

        elif _input == 'b':
            id = input("Enter the Employee ID: ")


    