"""
Contains the game loop and most of the top-level functions.
"""

from enum import Enum
from math_problem import MathProblem, inputNum
from operations import randomOperation


def main():
  input("Welcome to my Quiz!\n")
  while True:
    # Initiates the game loop
    selectDifficulty()
    quiz = Quiz(QUIZ_DIFFICULTY.value)
    quiz.play()

    # Prompts for another round
    if shouldPlayAgain() == False:
      print("Thanks for playing!")
      break


QUIZ_DIFFICULTY = None
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
    
  
  def newItem(self, ):
    """Generates a new math problem for the user to solve. Gives 2 chances by default"""
    problem = MathProblem(self.difficulty, randomOperation())

    attempts = 2
    chances = attempts

    while attempts > 0:
      answer = problem.ask()
      print("")

      if problem.checkAnswer(answer) == True:
        score = round(10 * (chances / attempts))
        print(f"Correct! You add {score:,} to your score")
        self.score += score
        break
      else:
        chances -= 1

      if attempts - chances == 1:
        print("Sucks, gotta try again.")
      elif attempts > 0:
        print("Still wrong.")
      else:
        print(f"Still wrong! Sorry, but the answer was {problem.key:,}.")


  def showScore(self, finalTally=False):
    """Prints out the current / final score on the terminal"""
    if finalTally:
      max = self.numberOfItems*10
      print(f"Your final score is {self.score:,} out of {max:,}.")
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
  global QUIZ_DIFFICULTY
  print("Select a difficulty:")

  # Lists out all the difficulties
  for i, difficulty in enumerate(list(Difficulties), start=1):
    print(f"{i}. {difficulty.name.capitalize()}")

  # Only accepts values in range before setting new difficulty
  while True:
    _ = inputNum("> ", acceptFloat=False)
    if _ not in range(1, i+1):
      continue

    QUIZ_DIFFICULTY = list(Difficulties)[_-1]
    print(f"\nDifficulty is set to {list(Difficulties)[_-1].name.capitalize()}.\n")
    break
  

if __name__ == "__main__":
  main()