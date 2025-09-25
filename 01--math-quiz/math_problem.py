"""
Contains all the logic for individual math problems.
"""

from enum import Enum
from operations import Operation, randomOperation
from random import randint


class Difficulties(Enum):
    """The values correspond to the number of digits in the operands."""
    EASY = 1
    MODERATE = 2
    ADVANCED = 4


def randomMathProblem(difficultyValue: int):
    operation = randomOperation()
    x = randomNum(difficultyValue)
    y = None
    if not operation.isComplex or difficultyValue <= 1:
        y = randomNum(difficultyValue)
    elif difficultyValue >= 2:
        y = randomNum(difficultyValue // 2)

    return MathProblem(difficultyValue, operation, x=x, y=y)


class MathProblem:
    """Generates a math problem"""

    def __init__(self, operandDigitCount: int, operation: type[Operation], x=0, y=0):
        self.x = x if x else randomNum(operandDigitCount)
        self.y = y if y else randomNum(operandDigitCount)
        self.operation = operation(self.x, self.y)
        self.key = self.operation.operate()
    
    def equation(self, showKey: bool=True):
        """Returns the formatted mathematical expression"""
        operatorSymbol = self.operation.operator
        key = f" = {self.key:,}" if showKey else ""
        return f"{self.x:,} {operatorSymbol} {self.y:,}{key}"
    
    def ask(self):
        return f"What is {self.equation(showKey=False)}?"
    
    def checkAnswer(self, answer: int | float) -> bool:
        return answer == self.key


# Helper functions here

def randomNum(digits: int=1) -> int:
    """Returns a number with a specified number of digits. Defaults to one-digit numbers (1 to 9)"""
    num = ""
    for n in range(digits, 0, -1):
        # Generates an int digit-by-digit and concatenates as a string
        num += str(randint(0 if n < digits else 1, 9))
    # Converts to int once finished.
    return int(num)


def inputNum(prompt: str, acceptFloat=True) -> int | float:
    """Similar to `input()`, but will only accept `int` and/or `float`. Otherwise, prompt again."""
    while True:
        response = input(prompt).replace(",","")
        if acceptFloat:
            try: return float(response)
            except ValueError: pass
        else:
            try: return int(response)
            except ValueError: pass
