"""Example of using inheritance to model different employee types."""

from __future__ import annotations


class Employee:
    """Base employee that stores shared identification data."""

    def __init__(self, employee_id: int, name: str, base_salary: int) -> None:
        self.employee_id = employee_id
        self.name = name
        self._base_salary = base_salary

    @property
    def base_salary(self) -> int:
        return self._base_salary

    def calculate_pay(self) -> int:
        """Return the amount of money paid to the employee."""
        return self._base_salary

    def describe_role(self) -> str:
        return f"{self.name}({self.employee_id}) is a company employee."


class FullTimeEmployee(Employee):
    """Full-time employee with an additional yearly bonus."""

    def __init__(self, employee_id: int, name: str, base_salary: int, bonus: int) -> None:
        super().__init__(employee_id, name, base_salary)
        self.bonus = bonus

    def calculate_pay(self) -> int:
        return self.base_salary + self.bonus

    def describe_role(self) -> str:
        return f"Full-time employee {self.name} receives a yearly bonus."


class PartTimeEmployee(Employee):
    """Part-time employee compensated hourly."""

    def __init__(self, employee_id: int, name: str, hourly_rate: int, hours_worked: int) -> None:
        super().__init__(employee_id, name, hourly_rate * hours_worked)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self) -> int:
        return self.hourly_rate * self.hours_worked

    def describe_role(self) -> str:
        return f"Part-time employee {self.name} is paid hourly."


class Intern(Employee):
    """Intern receiving a fixed stipend."""

    def __init__(self, employee_id: int, name: str, stipend: int) -> None:
        super().__init__(employee_id, name, base_salary=0)
        self.stipend = stipend

    def calculate_pay(self) -> int:
        return self.stipend

    def describe_role(self) -> str:
        return f"Intern {self.name} receives a fixed stipend."


employees = [
    FullTimeEmployee(1001, "Kim", 4_500_000, 500_000),
    PartTimeEmployee(1002, "Lee", 25_000, 80),
    Intern(1003, "Park", 1_200_000),
]

for employee in employees:
    role = employee.describe_role()
    total_pay = employee.calculate_pay()
    print(f"{role} -> {total_pay:,} KRW")
