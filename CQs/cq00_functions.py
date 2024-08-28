"""my first challenge question!"""

__author__ = "730772504"


def mimic(message: str) -> str:
    """purpose of the function is to mimic whatever message you input"""
    return message


def main() -> None:
    """implements the high-level logic of your functioning by pulling together other functions from the code"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
