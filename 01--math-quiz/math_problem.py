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


def randomMathProblem(operandDigits: int):
    """Generate random values to operate on"""
    operation = randomOperation()
    x = randomNum(operandDigits)
    y = None
    if not operation.isComplex or operandDigits <= 1:
        y = randomNum(operandDigits)
    elif operandDigits >= 2:
        y = randomNum(operandDigits // 2)
    return MathProblem(x, y, operation)


class MathProblem:
    """Generates a math problem"""

    def __init__(self, x, y, operation: type[Operation]):
        self.x = x
        self.y = y
        self.operation = operation(self.x, self.y)
        self.key = self.operation.operate()
    
    def equation(self, showKey: bool=True):
        """Returns the formatted mathematical expression"""
        operatorSymbol = self.operation.operator
        key = f" = {self.key:,}" if showKey else ""
        return f"{self.x:,} {operatorSymbol} {self.y:,}{key}"
    
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
