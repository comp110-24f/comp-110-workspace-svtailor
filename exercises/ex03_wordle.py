"""exercise 03! a simplified wordle"""

__author__ = "730772504"


def main(secret: str) -> None:
    """entrypoint of the program and main game loop."""

    turn: int = 1
    won: bool = False
    user_guess: str = ""  # empty string so i can replace it w new guesses

    while turn <= 6:
        # uses an f string
        print(f"=== Turn {turn}/6 ===")
        user_guess = input_guess(len(secret))
        print(emojified(user_guess, secret))

        if user_guess == secret:
            won = True
            print(f"You won in {turn}/6 turns!")
            exit()

        turn += 1

    if won == False:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """prompts user to input a guess for the wordle"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")

    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return guess


def contains_char(test_word: str, test_char: str) -> bool:
    assert len(test_char) == 1
    """checks to see if an inputted character is present in word of any length"""
    index: int = 0

    while index < len(test_word):
        if test_word[index] == test_char:
            return True

        # don't add an elif that returns as false because then
        # the function returns as false when it shouldn't
        # it should only return as true or not true (false)

        index += 1


def emojified(guess: str, secret: str) -> str:
    """emojify the validity of the user guess compared to secret word"""

    assert len(guess) == len(secret)
    # error if guess word isn't the same length as secret word

    index: int = 0  # counts until

    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"

    emojified_guess: str = ""
    # creating an empty string to add emoji concat, will print at the end

    while index < len(secret):
        if guess[index] == secret[index]:
            emojified_guess += green_box
            index += 1

        elif contains_char(secret, guess[index]) == True:
            # calls on contains_char to check if guess contains the letter in question
            emojified_guess += yellow_box
            index += 1

        else:
            emojified_guess += white_box
            index += 1

    return emojified_guess


if __name__ == "__main__":
    main("codes")
