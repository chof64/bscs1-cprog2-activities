""" module3/salary.py

A program that computes the salary of an employee.

"""
print("salary.py\n")

work_hours = input("Enter hours worked: ")
work_rate = input("Enter rate per hour: ")

print(f"Salary: {(float(work_hours) * float(work_rate))*30}")
