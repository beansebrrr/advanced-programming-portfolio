from student import Student
from file_reader import readFile

STUDENTS = [Student.fromParsed(line) for line in readFile()]


def searchByName(name: str) -> list[Student]:
    _ = list(filter(lambda student: student.name == name, STUDENTS))
    if _: return _


def sortByScore(ascending = False):
    return sorted(STUDENTS, key=lambda student: student.generalAverage(), reverse=not ascending)

def sortByName(descending = False):
    return sorted(STUDENTS, key=lambda student: student.name, reverse=descending)


def getHighestScore():
    return [sortByScore()[0]]

def getLowestScore():
    return [sortByScore()[-1]]