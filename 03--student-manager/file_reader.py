from pathlib import Path

PARENT_DIR = Path(__file__).parent.resolve()
textFileDir = PARENT_DIR / "studentMarks.txt"

def readFile():
    """Return a list of all the students' information (also in a list)"""
    # Finds the 'studentMarks.txt' file
    if not textFileDir.is_file():
        raise FileNotFoundError("studentMarks.txt does not exist in this directory")
    students = []
    with open(textFileDir) as file:
        file.readline()
        for line in file:
            students += parseTextLine(line)
    return students
       

def parseTextLine(txt_line):
    """Formats the textline into manageable variables"""
    extracted = txt_line.split(",")
    # Although a number, I will not be performing arithmetic operations on studentId
    # I will keep it as a string.
    studentId = extracted[0]
    studentName = extracted[1]
    courseMarks = [int(score) for score in extracted[2:5]]
    examMarks = int(extracted[-1].replace("\n", ""))
    return [studentId, studentName, courseMarks, examMarks]
