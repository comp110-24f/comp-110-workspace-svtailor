"""Practice with conditionals, variables, and user input"""

___author___ = "730772504"


def guess_a_number() -> None:
    """a function that takes an input number and checks it against a secret number"""
    secret: int = 7
    x: str = input("Guess a number: ")
    # input is always stored as a string
    print("Your guess was " + str(x))

    if int(x) == secret:
        # convert guess to an int because you can't use str w/ rational operators
        print("You got it!")

    elif int(x) < secret:
        # convert secret to a string because you can only add str with str
        print("Your guess was too low! The secret number is " + str(secret))

    elif int(x) > secret:
        # could have used else because if the guess isn't equal to or less than the secret number, it must be greater than
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
