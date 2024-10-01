"""practice with importing, formats a pair of string into coordinates"""

__author__ = "730772504"


def get_coords(xs: str, ys: str) -> None:

    index_xs: int = 0
    index_ys: int = 0
    # variables for the index for looping

    while index_xs < len(xs):
        while index_ys < len(ys):
            print("(" + xs[index_xs] + "," + ys[index_ys] + ")")
            index_ys += 1
            # loops through the entire ys string with each letter of the xs string

        index_xs += 1
        index_ys = 0
        # need to reset the index counter to 0 so it will re-enter the inner while loop
