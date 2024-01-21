import pytest
from src.salary import generate_salary_report, Employee

# czy lista pracowaników zawiera rejestry

def test_is_list_empty():
    with pytest.raises(ValueError, match="Employee list is empty."):
        generate_salary_report([])

def test_is_format_invalid():
    with pytest.raises(ValueError, match="Invalid employee format."):
        employees = [Employee(name="dupa",hourly_rate="40",hours_worked="40")]
        generate_salary_report(employees)

def test_is_rate_negative():
    with pytest.raises(ValueError, match="Hourly rate"):
        employees = [Employee(name="dupa",hourly_rate=-40,hours_worked=40)]
        generate_salary_report(employees)

def test_are_hours_negative():
    with pytest.raises(ValueError, match="hours worked"):
        employees = [Employee(name="dupa",hourly_rate=40,hours_worked=-40)]
        generate_salary_report(employees)

def test_calculate_noovertime():
    employees = [Employee(name="dupa",hourly_rate=40,hours_worked=40)]
    salary = generate_salary_report(employees)
    result = salary["dupa"]["salary"]
    assert result == 1600

def test_calculate_overtime():
    employees = [Employee(name="dupa",hourly_rate=40,hours_worked=50)]
    salary = generate_salary_report(employees)
    result = salary["dupa"]["salary"]
    assert result == 2200