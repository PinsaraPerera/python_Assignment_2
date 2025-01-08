import os

class Employee:
    def __init__(self, id, name, salary, department):
        self.id = id
        self.name = name
        self.salary = salary
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
        self.keys = []
        self.load_file()

    def load_file(self):
        if os.path.exists('Employee_Management_System/data.txt'):
            with open('Employee_Management_System/data.txt', 'r') as file:
                data = file.read()
                records = data.split('\n')

                for record in records:
                    if record:
                        employee_detail = record.split(',')
                        employee_detail = [_val.strip() for _val in employee_detail]
                        _id, _name, _salary, _department = employee_detail

                        if _id not in self.keys:
                            self.employees.append({"id": _id, "name": _name, "salary": _salary, "department": _department})
                            self.keys.append(_id)

                file.close()

        else:
            raise FileNotFoundException("File is not found")

    def add_employee(self, employee: Employee):

        if employee and (employee.id not in self.keys):
            self.employees.append({"id": employee.id, "name": employee.name, "salary": employee.salary, "department": employee.department})
            self.keys.append(employee.id)
        else:
            raise EmployeeNotFoundException(f'{"Employee data is duplicated" if employee.id in self.keys else "Employee data not confirmed"}')

    def remove_employee(self, employee_id):
        
        if employee_id in self.keys:
            self.employees = [_employee for _employee in self.employees if _employee["id"] != employee_id]

    def update_employee(self, employee: Employee):

        for _employee in self.employees:
            if _employee["id"] == employee.id:
                # _employee["name"] = employee.name
                _employee["salary"] = employee.salary
                _employee["department"] = employee.department

                break

    def dislay_all(self):
        for index, _employee in enumerate(self.employees):
            print(f'\t{index+1}) {_employee['id']}, {_employee['name']}, {_employee['salary']}, {_employee['department']}\n')

    def save_to_file(self):
        content = ''
        with open('Employee_Management_System/data.txt', 'w') as file:
            for _employee in self.employees:
                content += f'{_employee['id']}, {_employee['name']}, {_employee['salary']}, {_employee['department']}\n'

            file.write(content)
            file.close()


if __name__ == "__main__":

    database = EmployeeDatabase()
    RUN = True
    
    while RUN:
        print("\n~~~~~~~~~~~ MENU ~~~~~~~~~~~~~~~")
        print("a) Add new Employees.")
        print("b) Remove employee.")
        print("c) Update employee detail(salary, department).")
        print("d) Display all employees.")
        print("e) Load records from a file.")
        print("f) Exit system\n")

        _input = input("Choose an option: ")

        if _input == 'a':
            id = input("Enter the ID: ")
            name = input("Enter the Name: ")
            salary = float(input("Enter the Salary: "))
            department = input("Enter the Department: ")

            employee = Employee(id, name, salary, department)
            print(employee.id, employee.name, employee.salary, employee.department)
            database.add_employee(employee=employee)

            save = input("Do you want to save changes: (y/n)").lower()

            if save == 'y':
                database.save_to_file()

            print("Employee Added Successfully")

        elif _input == 'b':
            id = input("Enter the Employee ID: ")

            database.remove_employee(id)

            save = input("Do you want to save changes: (y/n)").lower()

            if save == 'y':
                database.save_to_file()

            print("Employee removed successfully")

        elif _input == 'c':
            id = input("Enter the ID: ")
            # name = input("Enter the Name: ")
            salary = float(input("Enter the Salary: "))
            department = input("Enter the Department: ")

            employee = Employee(id, "", salary, department) # name is not a changeble option
            database.update_employee(employee=employee)

            save = input("Do you want to save changes: (y/n)").lower()

            if save == 'y':
                database.save_to_file()

            print("Employee updated successfully")

        elif _input == 'd':
            database.dislay_all()

        elif _input == 'e':
            database.load_file() 

        elif _input == 'f':
            RUN = False

        else:
            print("Please input valid option.\n")

        


    