"""
Contains the game loop and most of the top-level functions.
THIS IS WHAT YOU SHOULD RUN
"""

from enum import Enum
from math_problem import MathProblem, inputNum
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


class Difficulties(Enum):
    """The values correspond to the number of digits in the operands."""
    EASY = 1
    MODERATE = 2
    ADVANCED = 4


class Quiz:
    def __init__(self, difficulty, numberOfItems=10):
        self.difficulty = difficulty
        self.numberOfItems = numberOfItems
        self.score = 0


    def play(self):
        """Iterates through `n` math problems for the user to solve, tallying the scores to be revealed at the end"""
        for n in range(self.numberOfItems):
            print(f"{n+1}. ", end="")
            self.newItem()
            
            if n < self.numberOfItems-1:
                self.showScore()

        self.showScore(finalTally=True)
        
    
    def newItem(self):
        """Generates a new math problem for the user to solve."""
        problem = MathProblem(self.difficulty, randomOperation())
        ATTEMPTS = 2
        chances = ATTEMPTS
        while chances > 0:
            answer = problem.ask()
            print("")
            # Validation and scoring logic here.
            if problem.checkAnswer(answer) == True:
                # Max score is 10. Decreases every failed attempt.
                score = round(10 * (chances / ATTEMPTS))
                self.score += score
                print(f"Correct! You add {score:,} to your score")
                break
            else:
                chances -= 1

            # Message displayed depends on how many attempts you have left.
            if ATTEMPTS - chances == 1:
                print("Sucks, gotta try again.")
            elif chances > 0:
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