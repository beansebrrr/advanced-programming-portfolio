from file_reader import readFile
from student import Student
import tkinter as tk

# It looks so beautiful
STUDENTS = [Student.fromParsed(line) for line in readFile()]


class StudentCard(tk.Frame):
    def __init__(self, master: tk, student: Student):
        super().__init__(master)
        self.config(
            border=6,
            relief=tk.RAISED,
            padx=24,
            pady=16,
        )

        self.columnconfigure(0, weight=1, minsize=150)
        self.columnconfigure(1, weight=3)

        courseMarkStr = ""
        for mark in student.courseMarks:
            courseMarkStr += f"\u2022 {mark}\n"
        
        Field(self, "Name", student.name, 0)
        Field(self, "I.D. Number", student.idNum, 1)
        Field(self, "Course Marks", courseMarkStr, 2)
        Field(self, "Assessment Marks", student.examMarks, 3)


class Field:
    def __init__(self, master, name, value, row):
        tk.Label(
            master,
            text=name,
            anchor="nw",
            justify="left",
            pady=6,
            padx=12,
        ).grid(column=0, row=row, sticky=tk.E)

        tk.Label(
            master,
            text=value,
            anchor="nw",
            justify="left",
            font=("helvetica", 14),
            pady=6
        ).grid(column=1, row=row, sticky=tk.W)



root = tk.Tk()

for student in STUDENTS:
    StudentCard(root, student).pack(fill="x")
    

root.mainloop()