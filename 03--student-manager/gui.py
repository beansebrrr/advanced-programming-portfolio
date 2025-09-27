from components import *
from sort_filter import *
import tkinter as tk
from tkinter import ttk


rootWindow = tk.Tk()
rootWindow.geometry("720x480")
rootWindow.title("Student Manager")
rootWindow.config(padx=12, pady=12)
studentList = StudentList(rootWindow)

def main():
    # Filtering
    filterFrame = tk.Frame(rootWindow, pady=2)
    studentSelector = StudentSelector(filterFrame)
    showAllBtn = tk.Button(
        filterFrame,
        text="Show All Students",
        command=studentList.displayStudents
    )
    

    sortFrame = tk.Frame(rootWindow, pady=2)
    highestScoreBtn = tk.Button(
        sortFrame,
        text="Highest Score",
        command=displayHighestScore
    )
    lowestScoreBtn = tk.Button(
        sortFrame,
        text="Lowest Score",
        command=displayLowestScore
    )

    # Sorting
    sortByNameBtn_asc = tk.Button(
        sortFrame,
        text="Ascending",
        command=displaySortedByName_asc
    )
    sortByNameBtn_desc = tk.Button(
        sortFrame,
        text="Descending",
        command=displaySortedByName_desc
    )


    studentSelector.pack(side="left")
    showAllBtn.pack(side="right")
    highestScoreBtn.pack(side="left")
    lowestScoreBtn.pack(side="left")

    sortByNameBtn_desc.pack(side="right")
    sortByNameBtn_asc.pack(side="right")
    tk.Label(sortFrame, text="Sort by name", padx=12).pack(side="right")

    tk.Label(
        rootWindow,
        text="Student Manager",
        font=("mono", 16, "bold"),
    ).pack()
    # Spacer
    tk.Frame(rootWindow, height=24).pack()
    filterFrame.pack(fill="x")
    sortFrame.pack(fill="x")
    # Spacer
    tk.Frame(rootWindow, height=24).pack()
    studentList.pack(fill="both")

    rootWindow.mainloop()


class StudentSelector(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=0)

        self.studentSelector = ttk.Combobox(
            self,
            values=[student.name for student in STUDENTS],
        )
        self.studentSelector.set("Select a student")
        studentSelectorBtn = tk.Button(
            self,
            text="Find",
            command=self.select
        )

        self.studentSelector.grid(column=0, row=0)
        studentSelectorBtn.grid(column=1, row=0)


    def select(self):
        selectedStudent = self.studentSelector.get()
        if selectedStudent in [s.name for s in STUDENTS]:
            studentList.displayStudents(searchByName(selectedStudent))


def displayHighestScore():
    studentList.displayStudents(getHighestScore())

def displayLowestScore():
    studentList.displayStudents(getLowestScore())

def displaySortedByName_asc():
    studentList.displayStudents(sortByName())

def displaySortedByName_desc():
    studentList.displayStudents(sortByName(descending=True))

main()