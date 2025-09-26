from pathlib import Path
from textwrap import dedent
    

class Student:
    numOfCourses = 3
    courseMarksMax = 20
    examMarksMax = 100
    def __init__(self, idNum: str, name: str, courseMarks: list[int], examMarks: int):
        # Guard clauses
        if len(idNum) != 4 or not idNum.isdecimal():
            raise ValueError("Student's ID must be a 4-digit number")
        if len(courseMarks) != self.numOfCourses:
            raise ValueError("Course marks should only have 3 items")
        self.idNum = idNum
        self.name = name
        self.courseMarks = courseMarks
        self.examMarks = examMarks

    def announceInfo(self):
        """Prints out student's information into the console."""
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
        print(infoString)

    def generalAverage(self):
        totalMarks = sum(self.courseMarks) + self.examMarks
        maxMarks = self.examMarksMax + (self.courseMarksMax * self.numOfCourses)
        genAverage = round(totalMarks / maxMarks, 4)
        return genAverage
    
    def grades(self):
        generalAverage = self.generalAverage() * 100
        if generalAverage >= 70.00:
            return "A"
        elif 69.99 >= generalAverage >= 60.00:
            return "B"
        elif 59.99 >= generalAverage >= 50.00:
            return "C"
        elif 49.99 >= generalAverage >= 40.00:
            return "D"
        else:
            return "F"
