from math_problem import MathProblem, randomMathProblem
# import operations as op
import tkinter as tk


class QuestionFrame(tk.Frame):
    questionField = None

    def __init__(self, master):
        super().__init__(master)

    def updateQuestionField(self, equation: str):
        text = f"What is {equation} ?"
        if self.questionField:
            self.questionField.destroy()
    
        self.questionField = tk.Label(self,
                                      text=text,
                                      font=("TkDefaultFont", 18))
        self.questionField.pack()


class InputFrame(tk.Frame):


    def __init__(self, master):
        super().__init__(master)

        self.entryField = tk.Entry(self)
        submitBtn = tk.Button(self, text="Submit")
        self.entryField.pack()
        submitBtn.pack()

    def getEntryFieldInput(self):
        entry = self.entryField.get()
        entry = entry.replace(",","")
        try:
            try: return float(entry)
            except ValueError: pass
        except ValueError:
            try: return int(entry)
            except ValueError: pass
    

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.questionFrame = QuestionFrame(self)
        self.questionFrame.pack()

        self.questionFrame.updateQuestionField("12 * 3")

        self.inputFrame = InputFrame(self)
        self.inputFrame.pack(side="bottom")


quiz = QuizApp()
quiz.geometry("600x400")
quiz.mainloop()

