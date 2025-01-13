"""Practice with recursive functions."""

# create a recursive function called factorial


def factorial(n: int) -> int:

    if n < 0:
        raise ValueError("n must be a positive integer.")

    # base cases:
    elif n == 1 or n == 0:
        return 1

    # recursive case
    else:
        return n * factorial(n - 1)
