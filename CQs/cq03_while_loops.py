"""practice using a while loop over a string"""

___author___ = "730772504"


def num_instances(phrase: str, search_char: str) -> int:
    """function that counts the number of times a given character appears in a phrase"""

    count: int = 0
    # count is the number of times your char appears in the phrase
    index: int = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
            # add one to the count if your char appears in the phrase

        index = index + 1
        # add one to the index regardless so you can keep looping through the phrase

    return count
