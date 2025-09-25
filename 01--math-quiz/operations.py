"""
Here I put all of the math operations.
"""

from random import choice


def randomOperation():
    return choice([
        Addition,
        Subtraction,
        Multiplication,
        Division,
    ])

class Operation:
    """Is the blueprint for all math operations."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def operate(self):
        raise NotImplementedError("Subclasses must implement `operate()`.")


class Addition(Operation):
    operator = "+"
    isComplex = False
    def __init__(self, x, y):
        super().__init__(x, y)

    def operate(self):
        return self.x + self.y
    

class Subtraction(Operation):
    operator = "-"
    isComplex = False
    def __init__(self, x, y):
        super().__init__(x, y)

    def operate(self):
        return self.x - self.y


class Multiplication(Operation):
    operator = "\u00D7"
    isComplex = True
    def __init__(self, x, y):
        super().__init__(x, y)

    def operate(self):
        return self.x * self.y


class Division(Operation):
    operator = "\u00F7"
    isComplex = True
    def __init__(self, x, y):
        super().__init__(x, y)

    def operate(self):
        return round((self.x / self.y), 2)
