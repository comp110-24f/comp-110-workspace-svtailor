"""exercise06! practice with dictionary functions"""

__author__ = "730772504"


def invert(input: dict[str, str]) -> dict[str, str]:
    """should swap keys and values in a dict"""

    inverted_dict: dict[str, str] = {}

    for key in input:
        if input[key] in inverted_dict:
            raise KeyError("Cannot have duplicate keys!")

        inverted_dict[input[key]] = key

    return inverted_dict


def favorite_color(input: dict[str, str]) -> str:
    """counts the most frequently mentioned color given a dict of fav colors"""

    # track the number of times a color appears:
    frequency_dict: dict[str, int] = {}
    # creates an empty dict to track color and frequency

    for name in input:
        if input[name] in frequency_dict:
            frequency_dict[input[name]] += 1

        else:
            frequency_dict[input[name]] = 1

    max_count: int = 0
    # keeps track of the highest frequency
    max_color: str = ""
    # keeps track of the color that appeared the most

    for color in frequency_dict:
        # for each color, if its frequency is higher than the previously stored max
        # store highest frequency and color associated w it
        if frequency_dict[color] > max_count:
            max_count = frequency_dict[color]
            max_color = color

    return max_color


def count(input: list[str]) -> dict[str, int]:
    """return sa dictionary of frequency of elems in input list"""

    count_item: dict[str, int] = {}

    for elem in input:
        if elem in count_item:
            count_item[elem] += 1

        else:
            count_item[elem] = 1

    return count_item


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """produces a dict w key of letters and values of words that begin w that letter"""

    alphabet_dict: dict[str, list[str]] = {}
    # creates empty dict to append letters + words to

    for word in input_list:
        if word[0].lower() in alphabet_dict:
            # .lower() is a built-in function that returns lower case version of given string
            alphabet_dict[word[0].lower()] += [word]
            # adds word to list (value of alphabet_dict)

        else:
            alphabet_dict[word[0].lower()] = [word]
            # creates new list (value of alphabet_dict)

    return alphabet_dict


def update_attendance(log: dict[str, list[str]], day: str, name: str) -> None:

    if day in log:
        if name not in log[day]:
            log[day] += [name]

    else:
        log[day] = [name]
