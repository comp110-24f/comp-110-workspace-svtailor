"""practice with conditionals"""


def less_than_10(num: int) -> bool:
    """Tells me if num is less than 10"""
    if num < 10:
        print("small number!")
    else:
        print("big number!")
    print("have a lovely day like the bill withers song")
    # the above line only works because i took out the return statements in the if else things


def should_i_eat(hungry: bool) -> None:
    "Tells me whether or not to eat based on hunger"
    if hungry == True:  # conditional/boolean expression
        print("girl go eat")  # 'then' block
    else:
        print("go to the library perhaps?")  # 'else block'
    print("you are so brave :P")  # these are examples of inline commenting


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match :("


print(check_first_letter("suhani", "h"))
