"""example of dictionary syntax with ice cream order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evalutates to the number of entries
print(len(ice_cream))  # prints 3

# add key-value entry by directly assigning to a key
ice_cream["mint"] = 3

# access entries by their key
print(ice_cream["mint"])  # prints 3

# test if pbj is a key in ice_cream
has_pbj: bool = "pbj" in ice_cream
# created new variable assigned to boolean
# new syntax!!! <key> in <dict>, checks to see if x is in y, returns bool

# removing an entry
ice_cream.pop("strawberry")

# iterating over key in loop
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor} has {tally} orders")
