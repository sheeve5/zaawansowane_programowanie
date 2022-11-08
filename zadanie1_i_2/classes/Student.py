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

