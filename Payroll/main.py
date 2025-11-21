
class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def get_info(self) -> str:
        return f"Employee: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department

    def get_info(self) -> str:
        return (f"Manager: {self.name}, Salary: {self.salary}, Department: "
                f"{self.department}")

emp1 = Employee("kia", 150000.00)
emp2 = Manager("Mina", 200000.00, "Engineering")
print(emp1.get_info())
print(emp2.get_info())