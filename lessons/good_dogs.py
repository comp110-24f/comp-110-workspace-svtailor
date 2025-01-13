"""Practice with recursion over a list for quiz04! # dogs110"""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    is_good: bool = int(scores[idx]["score"]) >= thresh
    is_last: bool = idx == len(scores) - 1

    if is_good is True:
        if is_last is True:
            return True

        else:
            all_good(scores, thresh, idx + 1)

    else:
        return False


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]

print(all_good(pack, 8, 0))
