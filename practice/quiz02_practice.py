"""questions from function writing quiz practice"""


def odd_and_even(input: list[int]) -> list[int]:
    new_list: list[int] = list()

    for idx in range(0, len(input)):
        if idx % 2 == 0 and input[idx] % 2 == 1:
            new_list.append(input[idx])

    return new_list


# 19 in lists, dict, and loops reinforcement questions
def str_length(input: list[str]) -> dict[str, int]:
    new_dict: dict[str, int] = {}

    for idx in range(0, len(input)):
        new_dict[input[idx]] = len(input[idx])

    return new_dict


# 2 in lists, dict, and loops reinforcement questions
def print_dict() -> None:
    my_dict: dict[int, str] = {}

    my_dict = {
        8: "eight",
        0: "zero",
        3: "three",
        -1: "negative one",
    }

    my_dict.pop(3)

    cat: int = my_dict[0]

    print(f"Keys: {len(my_dict)}")
    print(f"Values: {len(my_dict)}")

    my_dict[8] = "zero"


# 20 in lists, dict, and loops reinforcement questions
def frequency(word: str) -> dict[str, int]:

    frequency_dict: dict[str, int] = {}

    for index in range(0, len(word)):
        if word[index] in frequency_dict:
            frequency_dict[word[index]] += 1

        else:
            frequency_dict[word[index]] = 1

    return frequency_dict


# 25 in lists, dict, and loops reinforcement questions
def length(input: dict[str, list[float]]) -> dict[str, int]:
    new_dict: dict[str, int] = {}

    for key in input:
        new_dict[key] = len(input[key])

    return new_dict
