from classes.Employee import Employee
from classes.Student import Student


class Order:
    employee: Employee
    student: Student
    books: list
    order_date: str

    def __str__(self):
        ret = ""
        for i in self.books:
            ret += i.title + ", "
        return "{} zamówił/a {} dnia {}. " \
               "\nZamówienie realizuje {} {}".format(
                    self.student.name,
                    ret,
                    self.order_date,
                    self.employee.first_name,
                    self.employee.last_name)

    def __init__(self, _employee: Employee, _student: Student,
                 _books: list, _order_date: str):
        self.student = _student
        self.books = _books
        self.employee = _employee
        self.order_date = _order_date
