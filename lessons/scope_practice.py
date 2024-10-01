""""practice with scopes"""


def remove_chars(msg: str, char: str) -> str:
    """returns a copy of the message with all instances of the character removed"""
    copy: str = ""  # set up empty string so we can copy values over
    index: int = 0

    while index < len(msg):
        # if the letter does not match the character we want to remove
        if msg[index] != char:
            copy = copy + msg[index]

        index += 1  # loop until end of msg

    return copy

if __name__ = "__main__"

    # create a new variable called word with value yoyo
    word: str = "yoyo"  # word is a GLOBAL variable

    # print the result of calling your function with msg = word and "y"
    print(remove_chars(word, "y"))
