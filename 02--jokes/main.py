from pathlib import Path
from random import choice, randint
from time import sleep

def main():
    # Finds the 'jokes.txt' file
    parent_dir = Path(__file__).parent.resolve()
    txt_dir = parent_dir / "jokes.txt"
    if not txt_dir.is_file():
        raise FileNotFoundError("jokes.txt does not exist in this directory")
    # Creates the `Jokes` object
    jokes_list = getJokes(txt_dir)
    jokes = Jokes(jokes_list)
    while True:
        # Format the response to be lenient in detecting "Alexa tell me a joke"
        response = input("I know you want me to tell a joke.\n[Say \"Alexa, tell me a joke\", and \"bye\" to exit]\n> ").lower()
        response = "".join(char for char in response if char not in ".!?,")
        if response == "alexa tell me a joke":
            jokes.sayJoke(jokes.randomJoke())
            # Funny haha's
            laugh()
        elif response == "bye":
            # Exit condition
            typeWrite("k bye.")
            quit()

 
class Jokes:
    """Contains all the jokes, and all of its related functions"""
    def __init__(self, jokes: list[list[str]]):
        self.jokes = jokes

    def sayJoke(self, joke: list[str]):
        """Asks the question part, and once `Enter` is pressed, shows the response."""
        input(f"{joke[0]}?")
        typeWrite(f"{joke[-1]} ", end="")

    def randomJoke(self):
        return choice(self.jokes)


def getJokes(txt_dir):
    """Returns a 2-dimensional array containing all the jokes and responses from a .txt file"""
    with open(txt_dir, "r") as txt_file:
        # Split all the jokes
        jokes = txt_file.read().split("\n")
        # Split the questions from the responses
        jokes = list(map(lambda joke: joke.split("?",), jokes))
        return jokes


def laugh():
    """Silly haha function that prints a random number of 'Ha's """
    hahas = "HA" * randint(15,20)
    typeWrite(hahas, timegap_ms=0.075, end="\n\n")
    sleep(0.5)


def typeWrite(text, end="\n", timegap_ms=0.10,):
    """A simple typewriter"""
    for char in text:
        print(char, end="", flush=True)
        sleep(timegap_ms)
    print("", end=end)


main()