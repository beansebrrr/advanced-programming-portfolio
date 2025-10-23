from file_reader import readJokesFile
from random import choice
from re import sub
import tkinter as tk


JOKES_LIST = readJokesFile()


class Menu(tk.Tk):
    """Menu screen that generates the `Joke` windows"""
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Alexa is funny")
        # Title screen
        header = tk.Frame(self, pady=24)
        title = tk.Label(
            header,
            font=("arial", 24, "bold"),
            text="Hi! I'm Alexa.")
        subtitle = tk.Label(
            header,
            font=("arial", 14,),
            foreground="#444444",
            text="Would you like to hear a joke? Say \"Alexa, tell me a joke.\"",
            wraplength=300
        )
        title.pack()
        subtitle.pack()
        header.pack()
        # Allows user to type stuff
        inputFrame = tk.Frame(self, pady=12, padx=12)
        inputFrame.columnconfigure(0, weight=2)
        inputFrame.columnconfigure(1, weight=1)
        self.entryField = tk.Entry(inputFrame, font=("arial", 14))
        # Allow user to hit `Enter` to submit
        self.entryField.bind("<Return>", self.submitEntry)
        self.btnSubmit = tk.Button(
            inputFrame,
            text="Submit",
            font=("arial", 14),
            command=self.submitEntry
        )
        self.entryField.grid(column=0, row=0)
        self.btnSubmit.grid(column=1, row=0)
        inputFrame.pack(side="bottom", fill="x")

    def submitEntry(self, e=None):
        # Get raw text without punctuation
        entryText = self.entryField.get()
        entryText = sub(r"[^\w\s]", "", entryText).lower()
        if entryText == "alexa tell me a joke":
            JokePopup(self)


class JokePopup(tk.Toplevel):
    """Pops up and shows a randomly chosen joke"""
    def __init__(self, master):
        super().__init__(master)
        self.geometry("300x300")
        self.joke = choice(JOKES_LIST)
        self.title(f"{self.joke[0]}?")
        self.displayText = tk.Label(
            self,
            text=f"{self.joke[0]}?",
            font=("arial", 18),
            wraplength=250,
            pady=48,
        )
        self.btnShowPunchline = tk.Button(
            self,
            text="?",
            font=("arial", 24),
            pady=12,
            command=self.showPunchline,
        )
        self.displayText.pack()
        self.btnShowPunchline.pack(fill="x", side="bottom")

    def showPunchline(self):
        """Triggers when the user hits the `?` button"""
        self.btnShowPunchline.destroy()
        self.displayText.config(
            text=self.joke[-1],
        )


if __name__ == "__main__":
    Menu().mainloop()