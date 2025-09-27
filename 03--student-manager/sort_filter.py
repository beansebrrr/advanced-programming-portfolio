from student import Student
from file_reader import readFile

STUDENTS = [Student.fromParsed(line) for line in readFile()]


def searchByName(name: str) -> list[Student]:
    _ = list(filter(lambda student: student.name == name, STUDENTS))
    if _: return _
