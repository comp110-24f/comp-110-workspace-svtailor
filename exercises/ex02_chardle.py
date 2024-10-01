"""exercise 02 - making a simpler wordle using if statements and while loops"""

__author__ = "730772504"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")

    if len(word) == 5:
        return word

    else:
        print("Error: Word must contain 5 characters.")
        exit()
        # exit function is built in and tells the program to quit at that point
        return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")

    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()

    return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)

    count: int = 0
    # count is the number of times the letter appears in the word

    if word[0] == letter:
        count = count + 1
        print(letter + " found at index 0")
        # for each of these, it adds 1 to the count if the letter is present
        # then it prints where the letter is found in the word

    if word[1] == letter:
        count = count + 1
        print(letter + " found at index 1")

    if word[2] == letter:
        count = count + 1
        print(letter + " found at index 2")

    if word[3] == letter:
        count = count + 1
        print(letter + " found at index 3")

    if word[4] == letter:
        count = count + 1
        print(letter + " found at index 4")

    if count == 0:
        # checks if the letter hasn't appeared in the word
        print("No instances of " + letter + " found in " + word)

    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)

    else:
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
