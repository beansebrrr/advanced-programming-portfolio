"""
Contains all the logic for individual math problems.
"""

from random import randint
from operations import Operation


class MathProblem:
    """Generates a math problem"""

    def __init__(self, operandDigitCount: int, operation: type[Operation]):
        self.x = randomNum(operandDigitCount)
        self.y = randomNum(operandDigitCount)
        self.operation = operation(self.x, self.y)
        self.key = self.operation.operate()
    
    def equation(self, showKey: bool=True):
        """Returns the formatted mathematical expression"""
        operatorSymbol = self.operation.operator
        key = f" {self.key:,}" if showKey else ""
        return f"{self.x:,} {operatorSymbol} {self.y:,} ={key}"
    
    def ask(self):
        return inputNum(f"What is {self.equation(showKey=False)} ")
    
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
