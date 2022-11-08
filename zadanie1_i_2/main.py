from classes.Student import Student
from classes.Book import Book
from classes.Order import Order
from classes.Library import Library
from classes.Employee import Employee


print("zadanie1")
student1 = Student('Adam', [90, 90, 20, 20, 0])
student2 = Student("Barbara", [75, 60, 45, 70])
student3 = Student("Cyprian", [50, 90])
print("{} ma oceny {}, czyli {}".format(
    student1.name,
    student1.marks,
    student1.is_passed()))
print("{} ma oceny {}, czyli {}".format(
    student2.name,
    student2.marks,
    student2.is_passed()))


print("\nzadanie2")
lib1 = Library(
    "Katowicka",
    "Chorzów",
    "00-000",
    "10:30 - 19:00",
    "+48 000 000 000")
lib2 = Library(
    "Chorzowska",
    "Katowice",
    "00-000",
    "8:00 - 16:00",
    "+48 000 000 000")

book1 = Book("Title1", lib1, "10.12.2000",  "Firstname", "Lastname", 200)
book2 = Book("Title2", lib1, "10.12.2000",  "Firstname", "Lastname", 200)
book3 = Book("Title3", lib1, "10.12.2000",  "Firstname", "Lastname", 200)
book4 = Book("Title4", lib1, "10.12.2000",  "Firstname", "Lastname", 200)
book5 = Book("Title5", lib1, "10.12.2000",  "Firstname", "Lastname", 200)

employee1 = Employee(
    "Firstname",
    "Lastname",
    "20.08.2021",
    "02.10.1996",
    "City",
    "Street",
    "00-000",
    "+48 000 000 000")
employee2 = Employee(
    "Firstname2",
    "Lastname2",
    "20.08.2021",
    "02.10.1996",
    "City",
    "Street",
    "00-000",
    "+48 000 000 000")
employee3 = Employee(
    "Firstname3",
    "Lastnam3",
    "20.08.2021",
    "02.10.1996",
    "City",
    "Street",
    "00-000",
    "+48 000 000 000")

order1 = Order(employee2, student3, [book5, book4], "20.10.2022")
order2 = Order(employee1, student2, [book1, book3], "12.10.2022")

print(order1)
print(order2)