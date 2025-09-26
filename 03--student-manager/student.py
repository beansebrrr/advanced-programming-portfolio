from textwrap import dedent


COURSE_MARKS_MAX = 20
EXAM_MARKS_MAX = 100
NUM_OF_COURSES = 3


class Student:

    def __init__(self, idNum: str, name: str, courseMarks: list[int], examMarks: int):
        # Guard clauses
        if len(idNum) != 4 or not idNum.isdecimal():
            raise ValueError("Student's ID must be a 4-digit number")
        if len(courseMarks) != NUM_OF_COURSES:
            raise ValueError("Course marks should only have 3 items")
        self.idNum = idNum
        self.name = name
        self.courseMarks = courseMarks
        self.examMarks = examMarks

    @classmethod
    def fromParsed(cls, parsedLine: list[str|int|list[int]]):
        """Creates a Student out of a parsed text line"""
        studentId = parsedLine[0]
        studentName = parsedLine[1]
        courseMarks = parsedLine[2]
        examMarks = parsedLine[3]
        return cls(studentId, studentName, courseMarks, examMarks)

    def info(self):
        """Returns a string of student's information."""
        # `dedent()` is just used for cleaner code formatting
        infoString = dedent(f"""\
            Name: {self.name}
            I.D. Number: {self.idNum}
            Course Marks:
        """)
        # Format the course marks as a list
        for mark in self.courseMarks:
            infoString += f"  - {mark}\n"
        # Continuation
        infoString += dedent(f"""\
            Exam marks: {self.examMarks}
            Final Grade: {self.generalAverage():.2%} | {self.grades()}
        """)
        return infoString

    def generalAverage(self):
        totalMarks = sum(self.courseMarks) + self.examMarks
        maxMarks = EXAM_MARKS_MAX + (COURSE_MARKS_MAX * NUM_OF_COURSES)
        genAverage = round(totalMarks / maxMarks, 4)
        return genAverage
    
    def grades(self):
        generalAverage = self.generalAverage() * 100
        if generalAverage >= 70.00:
            return "A"
        elif 70 > generalAverage >= 60.00:
            return "B"
        elif 60 > generalAverage >= 50.00:
            return "C"
        elif 50 > generalAverage >= 40.00:
            return "D"
        else:
            return "F"

