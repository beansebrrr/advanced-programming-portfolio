from main import MathProblem, randomOperation

def main():
  quiz = Quiz(Difficulty["Moderate"])
  quiz.start()


Difficulty = {
  "Easy": 1,
  "Moderate": 2,
  "Advanced": 4,
}


class Quiz:
  def __init__(self, difficulty):
    self.difficulty = difficulty
    self.score = 0

  def start(self, numberOfItems=10):
    for n in range(numberOfItems):
      print(f"{n+1}. ", end="")
      self.newItem()
      
      if n < numberOfItems-1:
        print(f"You now have a score of {self.score:,}\n")
    
    print(f"Your final score is {self.score:,} out of {numberOfItems*10:,}.")
    

  def newItem(self):
    problem = MathProblem(self.difficulty, randomOperation())
    attempts = 2
    while attempts > 0:
      answer = problem.ask()
      print("")
      if problem.checkAnswer(answer) == True:
        score = attempts * 5
        print(f"Correct! You add {score:,} to your score")
        self.score += attempts * 5
        break
      elif attempts > 1:
        print("Sucks, gotta try again.")
      else:
        print(f"Still wrong! Sorry, but the answer was {problem.key:,}")
      attempts -= 1


if __name__ == "__main__":
  main()