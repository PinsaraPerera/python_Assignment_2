
with open('Employee_Management_System/data.txt', 'r') as file:
    data = file.read()
    records = data.split('\n')


employee_list = []

for record in records:
    if record:
        employee_details = record.split(',')
        employee_details = [_attr.strip() for _attr in employee_details]
        _id, _name, _salary, _department = employee_details

        print(_id, _name, _salary, _department)
        # print(employee_details)
