from pathlib import Path
from textwrap import dedent


def main():
    # Finds the 'studentMarks.txt' file
    parent_dir = Path(__file__).parent.resolve()
    txt_dir = parent_dir / "studentMarks.txt"
    if not txt_dir.is_file():
        raise FileNotFoundError("studentMarks.txt does not exist in this directory")
    students = []
    with open(txt_dir, "r") as file:
        # Take out the `number of students` line
        file.readline()
        for line in file:
            # Turn the textlines into `Student` objects, line by line
            studentId, studentName, courseMarks, examMarks = extractText(line)
            newStudent = Student(studentId, studentName, courseMarks, examMarks)
            students.append(newStudent)
    for student in students:
        student.announceInfo()


def extractText(txt_line: str):
    """Formats the textline into manageable variables"""
    extracted = txt_line.split(",")
    # Although a number, I will not be performing arithmetic operations on studentId
    # I will keep it as a string.
    studentId = extracted[0]
    studentName = extracted[1]
    courseMarks = [int(score) for score in extracted[2:5]]
    examMarks = int(extracted[-1].replace("\n", ""))
    return studentId, studentName, courseMarks, examMarks
    

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
        

if __name__ == "__main__":
    main()