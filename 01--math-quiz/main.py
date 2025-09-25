"""
Contains the game loop and most of the top-level functions.
"""


from math_problem import MathProblem, Difficulties, inputNum
from operations import randomOperation


def main():
    # Intro
    input("Le math quiz!\n")
    while True:
        # Initiates the game loop
        difficulty = selectDifficulty()
        quiz = Quiz(difficulty.value)
        quiz.play()

        # Prompts for another round
        if shouldPlayAgain() == False:
            print("Thanks for playing!")
            break




class Quiz:
    """Carries all the math """
    score = 0
    
    def __init__(self, difficulty, numberOfItems=10):
        self.difficulty = difficulty
        self.numberOfItems = numberOfItems

    def play(self):
        """Iterates through `n` math problems for the user to solve, tallying the scores to be revealed at the end"""
        for n in range(self.numberOfItems):
            print(f"{n+1}. ", end="")
            self.generateProblem()   
            if n < self.numberOfItems-1:
                self.showScore()
        self.showScore(finalTally=True)
        
    
    def generateProblem(self):
        """Generates a new math problem for the user to solve."""
        problem = MathProblem(self.difficulty, randomOperation())
        ATTEMPTS = 2
        # Give the user `ATTEMPTS` attempts to solve the equation
        for attempt in range(ATTEMPTS):
            answer = problem.ask()
            if problem.checkAnswer(answer):
                points = round(10 * ((ATTEMPTS - attempt) / ATTEMPTS))
                self.score += points
                print(f"Correct! You add {points:,} to your score")
                break
            # Message displayed depends on how many attempts you have left.
            elif attempt == 0:
                print("Sucks, gotta try again.")
            elif attempt < ATTEMPTS-1:
                print("Still wrong.")
            else:
                print(f"Still wrong! Sorry, but the answer was {problem.key:,}.")


    def showScore(self, finalTally=False):
        """Prints out the current / final score on the terminal"""
        if finalTally:
            max = self.numberOfItems*10
            print(f"Your final score is {self.score:,} out of {max:,}.")
            # Score-dependent message.
            print("Next time, let's shoot for higher scores, yeah?" if self.score / max < 0.60
                else "Hey, great job! I'm proud of you.", end="\n\n")
        else:
            print(f"You currently have {self.score} points\n")


def shouldPlayAgain():
    """Is an `input()` function that only returns a `bool`"""
    while True:
        _ = input("Would you like to play again? [Y/n] ").lower()

        if _ in ["yes", "y", "true", "t"]:
            return True
        elif _ in ["no", "n", "false", "f"]:
            return False


def selectDifficulty():
    print("Select a difficulty:")
    # Lists out all the difficulties
    for i, difficulty in enumerate(list(Difficulties), start=1):
        print(f"{i}. {difficulty.name.capitalize()}")
    while True:
        # Only accepts valid selections before setting new difficulty
        _ = inputNum("> ", acceptFloat=False)
        if _ not in range(1, i+1):
            continue
        # Return the according difficulty     
        difficulty = list(Difficulties)[_-1]
        print(f"\nDifficulty is set to {list(Difficulties)[_-1].name.capitalize()}.\n")
        return difficulty
    

if __name__ == "__main__":
    main()