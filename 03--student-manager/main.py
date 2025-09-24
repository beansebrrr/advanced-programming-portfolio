"""
NOTES:
    - Student contains a name, ID, 3 course marks, and 1 exam mark
"""

from pathlib import Path


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
        student.announce()


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
    def __init__(self, idNum: str, name: str, courseMarks: list[int], examMarks: int):
        self.id = idNum
        self.name = name
        self.courseMarks = courseMarks
        self.examMarks = examMarks

    def announce(self):
        """Just to reveal info"""
        print(f"I'm {self.name} with id {self.id}.")
        print(f"scores: {[score for score in self.courseMarks]}")
        print(f"Exam score: {self.examMarks}\n")


if __name__ == "__main__":
    main()