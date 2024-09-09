"""trying to see if whatever is after the return in a function still counts"""


def division(x: int, y: int) -> float:
    return y / x
    print(y % x)


print(division(y=64, x=16))

print(int(64 / 16))
