from components import *
from sort_filter import *
import tkinter as tk
from tkinter import ttk


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("720x480")
        self.config(
            padx=12,
            pady=12,
        )
        self.studentList = StudentList(self)
        filterFrame = tk.Frame(
            self,
            pady=24
        )
        studentSelectorFrame = tk.Frame(
            filterFrame
        )
        studentSelectorFrame.columnconfigure(0, weight=2)
        studentSelectorFrame.columnconfigure(1, weight=0)

        self.studentSelector = ttk.Combobox(
            studentSelectorFrame,
            values=[student.name for student in STUDENTS],         
        )
        self.studentSelector.set("Select a student")
        studentSelectorButton = tk.Button(
            studentSelectorFrame,
            text="Find",
            command=self.search
        )
        showAllButton = tk.Button(
            filterFrame,
            text="Show All Students",
            command=self.studentList.displayStudents
        )

        self.studentSelector.grid(column=0, row=0)
        studentSelectorButton.grid(column=1, row=0)
        studentSelectorFrame.pack(side="left")
        showAllButton.pack(side="right")


        filterFrame.pack(anchor="w", fill="x")
        self.studentList.pack(fill="x")
    
    def search(self):
        searchTerm = self.studentSelector.get()
        if searchTerm in [student.name for student in STUDENTS]:
            self.studentList.displayStudents(
                searchByName(searchTerm)
            )


Root().mainloop()