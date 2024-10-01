"""file that defines a function that concatenates two strings"""

__author__ = "730772504"


def concat(first_word: str, second_word: str) -> str:
    # function that concatenates two inputted strings
    return first_word + second_word


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":

    # will only print if this file is the one being called
    print(concat(word1, word2))
