"""
Contains the logic for file-reading and parsing the
text file into a manageable data structure.
"""

from pathlib import Path


PARENT_DIR = Path(__file__).parent.resolve()
jokesDirectory = PARENT_DIR / "jokes.txt"


def readJokesFile():
    """Returns a 2-dimensional array containing all the jokes and responses from a .txt file"""
    with open(jokesDirectory) as file:
        # Split all the jokes
        jokes = file.read().split("\n")
        # Split the questions from the responses
        jokes = list(map(lambda joke: joke.split("?",), jokes))
        return jokes
