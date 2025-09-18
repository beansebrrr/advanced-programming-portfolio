from random import randint
from enum import Enum

def main():
  question = Question(Difficulty["Moderate"], Division)
  print(question.textContent())

Difficulty = {
  "Easy": 1,
  "Moderate": 2,
  "Advanced": 4,
}

class Question:
  def __init__(self, difficulty, operator):
    self.x = randomNum(difficulty)
    self.y = randomNum(difficulty)
    operation = operator(self.x, self.y)

    self.operator = operation.operator
    self.answer = operation.operate()
  
  def textContent(self):
    return f"{self.x} {self.operator} {self.y} = {self.answer}"


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
    return self.x / self.y


def randomNum(digits: int=1) -> int:
  """Returns a number with a specified number of digits. Defaults to one-digit numbers (1 to 9)"""
  num = 0
  for n in range(digits, 0, -1):
    # Generates an int digit-by-digit
    num += randint(0 if n < digits else 1, 9) * (10 ** (n-1))
  return num


main()