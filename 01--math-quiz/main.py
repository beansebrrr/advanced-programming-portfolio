from random import randint

def main():
  question = MathProblem(Difficulty["Moderate"], Subtraction)
  print(question.ask())


Difficulty = {
  "Easy": 1,
  "Moderate": 2,
  "Advanced": 4,
}

class MathProblem:
  def __init__(self, difficulty, operator):
    self.x = randomNum(difficulty)
    self.y = randomNum(difficulty)
    self.operation = operator(self.x, self.y)

    self.key = self.operation.operate()
  
  def textContent(self):
    return f"{self.x} {self.operation.operator} {self.y} = {self.key}"
  
  def ask(self):
    answer = inputNum(f"What is {self.x} {self.operation.operator} {self.y}? ")
    return answer == self.key


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


def randomNum(digits: int=1) -> int:
  """Returns a number with a specified number of digits. Defaults to one-digit numbers (1 to 9)"""
  num = 0
  for n in range(digits, 0, -1):
    # Generates an int digit-by-digit
    num += randint(0 if n < digits else 1, 9) * (10 ** (n-1))
  return num


def inputNum(prompt):
  while True:
    _ = input(prompt)
    try: return int(_)
    except ValueError: pass
    try: return float(_)
    except ValueError: pass

if __name__ == "__main__":
  main()