from math_problem import MathProblem
import operations as op
import tkinter as tk



class QuizApp:

    rootWindow = tk.Tk()
    rootWindow.geometry("600x400")

    userInput = tk.StringVar()

    def __init__(self):
        # self.displayMathProblem()

        entryField = tk.Entry(self.rootWindow, textvariable=self.userInput)
        entryField.pack()

        buttonPrint = tk.Button(text="Read input", command=self.printEntry)
        buttonPrint.pack()

        self.rootWindow.mainloop()

    def displayMathProblem(self, mathProblem: MathProblem):
        equation = mathProblem.equation(showKey=False)
        text = f"What is {equation}?"

        questionLabel = tk.Label(self.rootWindow, text=text)
        questionLabel.pack()

    def printEntry(self):
        print(self.userInput.get())








newQuiz = QuizApp()
