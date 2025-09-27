from student import Student
from sort_filter import STUDENTS
import tkinter as tk
from tkinter import ttk


class StudentList(ttk.Frame):
    def __init__(self, parent, *args, **kw):
        """Credit for scrollable frames: https://stackoverflow.com/a/16198198"""
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        scrollbar = ttk.Scrollbar(self, orient="vertical")
        scrollbar.pack(fill="y", side="right", expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=tk.TRUE)
        scrollbar.config(command=canvas.yview)

        # Reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.innerFrame = innerFrame = ttk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=innerFrame,
                                           anchor=tk.NW)

        self.displayStudents(STUDENTS)

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (innerFrame.winfo_reqwidth(), innerFrame.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if innerFrame.winfo_reqwidth() != canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                canvas.config(width=innerFrame.winfo_reqwidth())
        innerFrame.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if innerFrame.winfo_reqwidth() != canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


    def displayStudents(self, students: list[Student]=STUDENTS):
        """Displays student cards generated from a filtered list of students.
        Defaults to displaying all students."""
        self.clear()
        for student in students:
            StudentCard(self.innerFrame, student).pack(fill="x")
            tk.Frame(self.innerFrame, height=12).pack()

        
    def clear(self):
        """Delete all child elements"""
        for child in self.innerFrame.winfo_children():
            child.destroy()


class StudentCard(tk.Frame):
    """Card displaying a student's information."""
    def __init__(self, master: tk, student: Student):
        super().__init__(master)
        # Make it look like a card
        self.config(
            border=12,
            padx=24,
            pady=16,
            relief="groove"
        )
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)

        # Formatting the courseMarks list to a string
        courseMarkStr = ""
        for mark in student.courseMarks:
            courseMarkStr += f"\u2022 {mark}\n"
        
        # Basic student info here
        createField(self, "Name", student.name, 0)
        createField(self, "I.D. Number", student.idNum, 1)
        createField(self, "Course Marks", courseMarkStr, 2)
        createField(self, "Assessment Marks", student.examMarks, 3)

        # Shows off the student's grade 
        gradeFrame = tk.Frame(self)
        grade = tk.Label(
            gradeFrame,
            text=f"{student.grades()}",
            font=("Times New Roman", 32, "bold"))
        percentage = tk.Label(
            gradeFrame,
            text=f"General Average\nof {student.generalAverage():.2%}",
            font=("mono", 12))
        
        grade.pack(anchor="center")
        percentage.pack(anchor="center")
        gradeFrame.grid(column=2, row=0, rowspan=4)


def createField(master, name, value, row):
    """Student info field."""
    tk.Label(
        master,
        text=name,
        anchor="nw",
        justify="left",
        font=("mono", 12),
        pady=6,
        padx=12,
    ).grid(column=0, row=row, sticky=tk.NW)

    tk.Label(
        master,
        text=value,
        anchor="nw",
        justify="left",
        font=("serif", 14),
        pady=6,
    ).grid(column=1, row=row, sticky=tk.NW)