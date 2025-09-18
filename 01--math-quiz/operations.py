"""
Here I put all of the math operations.
If needed, I can create other operations like say, exponents.
"""

from random import choice


def randomOperation():
  return choice([
    Addition,
    Subtraction,
    Multiplication,
    Division,
  ])


class Addition:
  def __init__(self, x, y):
    self.operator = "+"
    self.x = x
    self.y = y

  def operate(self):
    return self.x + self.y
  

class Subtraction:
  def __init__(self, x, y):
    self.operator = "-"
    self.x = x
    self.y = y

  def operate(self):
    return self.x - self.y


class Multiplication:
  def __init__(self, x, y):
    self.operator = "*"
    self.x = x
    self.y = y

  def operate(self):
    return self.x * self.y


class Division:
  def __init__(self, x, y):
    self.operator = "/"
    self.x = x
    self.y = y

  def operate(self):
    return round((self.x / self.y), 2)
