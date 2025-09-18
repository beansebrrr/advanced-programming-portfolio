"""
Contains all the logic for individual math problems.
"""

from random import randint


class MathProblem:
  def __init__(self, operandDigitCount: int, operator):
    self.x = randomNum(operandDigitCount)
    self.y = randomNum(operandDigitCount)
    self.operation = operator(self.x, self.y)

    self.key = self.operation.operate()
  
  def equation(self, showKey: bool=True):
    """Returns the mathematical expression"""
    return f"{self.x:,} {self.operation.operator} {self.y:,} ={f" {self.key:,}" if showKey else ""}"
  
  def ask(self):
    return inputNum(f"What is {self.equation(showKey=False)} ")
  
  def checkAnswer(self, answer: int | float) -> bool:
    return answer == self.key


def randomNum(digits: int=1) -> int:
  """Returns a number with a specified number of digits. Defaults to one-digit numbers (1 to 9)"""
  num = 0
  for n in range(digits, 0, -1):
    # Generates an int digit-by-digit
    num += randint(0 if n < digits else 1, 9) * (10 ** (n-1))
  return num


def inputNum(prompt: str, acceptFloat=True) -> int | float:
  """Similar to `input()`, but will only accept `int` and/or `float`. Otherwise, prompt again."""
  while True:
    _ = input(prompt).replace(",","")

    try: return int(_)
    except ValueError: pass

    if acceptFloat:
      try: return float(_)
      except ValueError: pass


if __name__ == "__main__":
  pass