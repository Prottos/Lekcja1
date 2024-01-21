from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    hourly_rate: float
    hours_worked: float

dupa = Employee("dupa", 40, 40)
print(dupa)