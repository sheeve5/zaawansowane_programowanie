class Student:
    name: str
    marks: list

    def __init__(self, _name: str, _marks: list):
        self.name = _name
        self.marks = _marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50

    def __str__(self):
        return self.name


class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str

    def __str__(self):
        return "Adres: ulica {}, w {}, kod pocztowy {}\nGodziny otwarcia: {}\nNr telefonu: {}".format(self.street,
                                                                                                      self.city,
                                                                                                      self.zip_code,
                                                                                                      self.open_hours,
                                                                                                      self.phone)

    def __init__(self, _street: str, _city: str, _zip_code: str, _open_hours: str, _phone: str):
        self.city = _city
        self.street = _street
        self.zip_code = _zip_code
        self.open_hours = _open_hours
        self.phone = _phone


class Employee:
    first_name: str
    last_name: str
    hire_date: str
    birth_date: str
    city: str
    street: str
    zip_code: str
    phone: str

    def __str__(self):
        return "{} {}, zatrudniony/a {}, urodzony/a {}\nAdres zamieszkania: ul {} w {}, kod pocztowy {}\nNr telefonu: {}".format(
            self.first_name,
            self.last_name,
            self.hire_date,
            self.birth_date,
            self.street,
            self.city,
            self.zip_code,
            self.phone)

    def __init__(self, _first_name: str, _last_name: str, _hire_date: str, _birth_date: str, _city: str, _street: str,
                _zip_code: str, _phone: str):
        self.first_name = _first_name
        self.last_name = _last_name
        self.hire_date = _hire_date
        self.birth_date = _birth_date
        self.street = _street
        self.city = _city
        self.zip_code = _zip_code
        self.phone = _phone

class Book:
    title: str
    library: Library
    publication_date: str
    author_name: str
    author_surname: str
    number_of_pages: int

    def __str__(self):
        return "{}, Autor: {} {}, Biblioteka przy ulicy {} w {}, data publikacji {}, {} stron".format(self.title,
                                                                                                      self.author_name,
                                                                                                      self.author_surname,
                                                                                                      self.library.street,
                                                                                                      self.library.city,
                                                                                                      self.publication_date,
                                                                                                      self.number_of_pages)

    def __init__(self, _title: str, _library: Library, _publication_date: str, _author_name: str, _author_surname: str,
                 _number_of_pages: int):
        self.title = _title
        self.author_name = _author_name
        self.author_surname = _author_surname
        self.library = _library
        self.publication_date = _publication_date
        self.number_of_pages = _number_of_pages


class Order:
    employee: Employee
    student: Student
    books: list
    order_date: str

    def __str__(self):
        ret = ""
        for i in self.books:
            ret += i.title + ", "
        return "{} zamówił/a {} dnia {}. Zamówienie realizuje {} {}".format(self.student.name, ret, self.order_date, self.employee.first_name, self.employee.last_name)

    def __init__(self, _employee: Employee, _student: Student, _books: list, _order_date: str):
        self.student = _student
        self.books = _books
        self.employee = _employee
        self.order_date = _order_date

print("zadanie1")
student1 = Student('Adam', [90, 90, 20, 20, 0])
student2 = Student("Barbara", [75, 60, 45, 70])
student3 = Student("Cyprian", [50, 90])
print("{} ma oceny {}, czyli {}".format(student1.name, student1.marks, student1.is_passed()))
print("{} ma oceny {}, czyli {}".format(student2.name, student2.marks, student2.is_passed()))


print("\nzadanie2")
lib1 = Library("Katowicka", "Chorzów", "00-000", "10:30-19:00", "+48 000 000 000")
lib2 = Library("Chorzowska", "Katowice", "00-000", "8:00-16:00", "+48 000 000 000")

book1 = Book("Title1", lib1, "10.12.2000",  "Firstname", "Lastname", 200)
book2 =Book("Title2", lib1, "10.12.2000",  "Firstname", "Lastname", 200)
book3 = Book("Title3", lib1, "10.12.2000",  "Firstname", "Lastname", 200)
book4 = Book("Title4", lib1, "10.12.2000",  "Firstname", "Lastname", 200)
book5 = Book("Title5", lib1, "10.12.2000",  "Firstname", "Lastname", 200)

employee1 = Employee("Firstname", "Lastname", "20.08.2021", "02.10.1996", "City", "Street", "00-000", "+48 000 000 000")
employee2 = Employee("Firstname2", "Lastname2", "20.08.2021", "02.10.1996", "City", "Street", "00-000", "+48 000 000 000")
employee3 = Employee("Firstname3", "Lastnam3", "20.08.2021", "02.10.1996", "City", "Street", "00-000", "+48 000 000 000")

order1 = Order(employee2, student3, [book5, book4], "20.10.2022")
order2 = Order(employee1, student2, [book1, book3], "12.10.2022")

print(order1)
print(order2)