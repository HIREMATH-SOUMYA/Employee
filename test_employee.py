# test_employee.py
import pytest
from employee import get_employee_info

def test_get_employee_info():
    # Sample input
    name = "John Doe"
    emp_id = "E101"
    department = "IT"
    salary = 55000

    # Expected formatted output
    expected_output = (
        "Employee Name: John Doe\n"
        "Employee ID: E101\n"
        "Department: IT\n"
        "Salary: 55000.00"
    )

    # Assert test
    assert get_employee_info(name, emp_id, department, salary) == expected_output