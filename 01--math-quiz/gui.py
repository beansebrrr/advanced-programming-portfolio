from math_problem import randomMathProblem, Difficulties
import tkinter as tk
from tkinter import ttk


NUM_OF_ITEMS = 10
MAX_ATTEMPTS = 2
MAX_SCORE_PER_ITEM = 10


class StartScreen(tk.Tk):
    """Difficulty selector. Will create all the quizzes"""
    
    difficultyList = [diff.name.capitalize() for diff in Difficulties]
    def __init__(self):
        super().__init__()
        self.title("Vince's Perfect Math Class")
        self.geometry("300x300")
        self.resizable(0, 0)

        header = tk.Label(self,
                          text="Welcome to Vince's Perfect Math Class",
                          font=("mono", 18, "bold"),
                          wraplength=280,
                          pady=48)

        self.difficultySelector = ttk.Combobox(self,
                                               values=self.difficultyList,
                                               font=("mono", 12))  
        self.difficultySelector.set("Choose a difficulty")
        btnStartQuiz = tk.Button(self,
                                 text="Start Quiz",
                                 font=("mono", 14),
                                 command=self.createQuiz)
        
        header.pack(fill="x")
        self.difficultySelector.pack()
        tk.Frame(self,height=24).pack()
        btnStartQuiz.pack()


    def createQuiz(self):
        selected = self.difficultySelector.get()
        if selected in self.difficultyList:
            difficulty = Difficulties.__getitem__(selected.upper())
            QuizApp(difficulty).mainloop()


class QuizApp(tk.Toplevel):
    """All the logic for the Math's quiz"""
    currentItem = 0
    currentScore = 0

    def __init__(self, difficulty):
        # Initialize the root window
        super().__init__()
        self.title("Quiz!")
        self.geometry("600x400")
        self.resizable(0, 0)
        self.difficulty = difficulty
        # Build its child elements
        self.questionLabel = tk.Label(self, font=("mono", 18), pady=24)
        self.messageBoard = MessageBoard(self)
        self.inputFrame = InputFrame(self)
        # Start the loop right away
        self.showNextQuestion()
        self.questionLabel.pack()
        self.inputFrame.pack(side="bottom", fill="x")
        self.messageBoard.pack(side="bottom")

        self.grab_set()
    
    def displayQuizResult(self):
        # Delete everything currently on the window
        self.questionLabel.destroy()
        self.messageBoard.destroy()
        self.inputFrame.destroy()

        maxScore = NUM_OF_ITEMS * MAX_SCORE_PER_ITEM
        scoreColor = "green" if self.currentScore > (maxScore * 0.50) else "red"

        frame = tk.Frame(self)
        toptextLabel = tk.Label(frame,
                               text="Your final grade is",
                               font=("TkDefaultFont", 14))
        resultLabel = tk.Label(frame,
                               text=self.getGrade(),
                               font=("TkDefaultFont", 24, "bold"),
                               foreground=scoreColor,)
        subtextLabel = tk.Label(frame,
                                text=f"{self.currentScore} out of {maxScore}",
                                font=("TkDefaultFont", 14))
        toptextLabel.pack()
        resultLabel.pack()
        subtextLabel.pack()
        frame.pack(pady=100)

    def getGrade(self):
        average = (self.currentScore / (NUM_OF_ITEMS * MAX_SCORE_PER_ITEM)) * 100
        if average >= 90:
            return "A"
        elif 70 <= average < 90:
            return "B"
        elif 60 <= average < 70:
            return "C"
        elif 50 <= average < 60:
            return "D"
        else:
            return "F"
        

    def questionResult(self, answerIsCorrect: bool):
        if answerIsCorrect:
            # Score decreases every failed attempt for each item
            score = round(MAX_SCORE_PER_ITEM * (self.attempts / MAX_ATTEMPTS))
            message = f"Congratulations! You got it right! Your score went up by {score}"
            self.messageBoard.goodMessage(message)
            self.currentScore += score
            self.inputFrame.showBtnNext()
        else:
            self.attempts -= 1
            if self.attempts > 0:
                message = f"Quite wrong! You have {self.attempts} more {"tries" if self.attempts > 1 else "try"}."
                self.messageBoard.badMessage(message)
            else:
                # Only reveal the answer when 0 attempts left
                message = f"Oof! The answer is actually {self.currentMathProblem.key}."
                self.messageBoard.badMessage(message)
                self.inputFrame.showBtnNext()
        self.inputFrame.clearEntryField()

    def showNextQuestion(self):
        # Breaks right away if there are no more math problems to solve
        if self.currentItem == NUM_OF_ITEMS:
            self.displayQuizResult()
            return
        # Resets the attempts counter
        self.attempts = MAX_ATTEMPTS
        self.currentItem += 1
        # Update the quiz item
        self.updateMathProblem()
        newEquation = self.currentMathProblem.equation(showKey=False)
        self.questionLabel.config(text=f"{self.currentItem}. What is {newEquation} ?")
        self.inputFrame.showBtnSubmit()
        self.messageBoard.clear()

    def updateMathProblem(self):
        self.currentMathProblem = randomMathProblem(self.difficulty.value)

    def checkEntry(self):
        answer = self.inputFrame.getEntryFieldInput()
        if answer == None:
            self.messageBoard.badMessage("Please enter a number.")
            return
        isCorrect = self.currentMathProblem.checkAnswer(answer)
        self.questionResult(isCorrect)


class MessageBoard(tk.Label):
    """Informs the user of invalid inputs, correct answers, and such"""

    def __init__(self, master):
        super().__init__(master,
                         font=("mono", 14),
                         pady=12,
                         wraplength=550)

    def clear(self):
        self.config(text="")

    def goodMessage(self, text):
        self.config(text=text, foreground="green")

    def badMessage(self, text):
        self.config(text=text, foreground="red")


class InputFrame(tk.Frame):
    """Contains everything user input-related"""
    def __init__(self, master):
        super().__init__(master)
        # Create all input elements
        self.entryField = tk.Entry(self, font=("mono", 16))
        self.btn = tk.Button(self, font=("mono", 12))
        self.showBtnSubmit()
        self.entryField.pack(fill="x")
        self.btn.pack(fill="x")

    def clearEntryField(self):
        self.entryField.delete(0, tk.END)

    def showBtnNext(self):
        """Button to bring user to the next math problem"""
        txt = "Next problem" if self.master.currentItem < NUM_OF_ITEMS else "See results"
        self.btn.config(text=txt, command=self.master.showNextQuestion)

    def showBtnSubmit(self):
        """Button to submit your answer"""
        self.btn.config(text="Submit", command=self.master.checkEntry)

    def getEntryFieldInput(self):
        """Convert entry's string into an int or float"""
        entry = self.entryField.get()
        entry = entry.replace(",","")
        
        try:
            return int(entry)
        except ValueError: 
            try: return float(entry)
            except ValueError: pass



if __name__ == "__main__":
    StartScreen().mainloop()
