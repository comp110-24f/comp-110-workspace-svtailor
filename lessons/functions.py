"""practice with functions"""

from random import randint

print(randint(1, 100))


# function defintion
def sum(num1: int, num2: int) -> int:
    """return the sum of num1 and num2"""
    return num1 + num2


# function call
print(sum(num1=7, num2=94))

# when we function call, we input our ARGUMENTS (num1 = 2, num2 = 4)
