from random import randint, choice

class MathProblem:
  def __init__(self, difficulty, operator):
    self.x = randomNum(difficulty)
    self.y = randomNum(difficulty)
    self.operation = operator(self.x, self.y)

    self.key = self.operation.operate()
  
  def equation(self, showKey=True):
    return f"{self.x:,} {self.operation.operator} {self.y:,} ={f" {self.key:,}" if showKey else ""}"
  
  def ask(self):
    return inputNum(f"What is {self.equation(showKey=False)} ")
  
  def checkAnswer(self, answer:int|float):
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

def randomOperation():
  return choice([Addition, Subtraction, Multiplication, Division])

def inputNum(prompt):
  while True:
    _ = input(prompt)
    try: return int(_)
    except ValueError: pass
    try: return float(_)
    except ValueError: pass

if __name__ == "__main__":
  question = MathProblem(2, Subtraction)
  print(randomOperation())