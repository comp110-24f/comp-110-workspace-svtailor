"""practice with for loops"""

pets: list[str] = ["Louie", "Bo", "Bear"]


for name in pets:
    print(f"Good boy, {name}!")

# same output using range:
for index in range(0, len(pets)):
    print(f"Good boy, {pets[index]}!")

# using range() in a for...in... loop:

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for index in range(0, len(names)):
    print(f"{index}: {names[index]}")
